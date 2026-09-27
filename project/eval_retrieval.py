import argparse
import json
import re
from typing import Dict, List, Sequence, Set, Tuple

import config
from db.vector_db_manager import VectorDbManager


# First golden sample based on the user's real question.
DEFAULT_SAMPLE = {
    "name": "computer_track_courses",
    "query": "计算机技术专业可选的专业学位课、非学位课有哪些",
    "source": "电子信息培养方案.pdf",
    "gold_codes": [
        # Professional degree courses (direction 2 + shared direction 1-6)
        "081000mb07",
        "081200mb16",
        "081203mb06",
        "083500mb02",
        "085400mb11",
        "081200mb03",
        "085400mb03",
        "085400mb01",
        # Non-degree courses (direction 2 related)
        "081200mc01",
        "081200mc24",
        "081201mc01",
        "085400mc12",
        "430112mc14",
    ],
}


def normalize_code(code: str) -> str:
    return code.strip().upper()


def extract_course_codes(text: str) -> Set[str]:
    # Matches patterns like 081000mb07 / 0812Z3mc01 / 430112mc14
    pattern = re.compile(r"\b[0-9A-Za-z]{8,12}\b")
    return {normalize_code(item) for item in pattern.findall(text)}


def get_ranked_chunks(query: str, top_k: int, collection=None):
    if collection is None:
        vector_db = VectorDbManager()
        collection = vector_db.get_collection(config.CHILD_COLLECTION)
    try:
        return collection.similarity_search_with_score(query, k=top_k)
    except Exception:
        docs = collection.similarity_search(query, k=top_k)
        return [(doc, None) for doc in docs]


def evaluate_retrieval(
    query: str,
    gold_codes: Sequence[str],
    top_k: int = 8,
    source_filter: str | None = None,
    collection=None,
) -> Tuple[Dict[str, float], List[Dict[str, object]]]:
    ranked = get_ranked_chunks(query, top_k, collection=collection)
    gold_set = {normalize_code(code) for code in gold_codes}

    retrieved_chunks: List[Dict[str, object]] = []
    predicted_codes: Set[str] = set()
    first_relevant_rank: int | None = None

    for idx, (doc, score) in enumerate(ranked, start=1):
        source = str(doc.metadata.get("source", ""))
        if source_filter and source != source_filter:
            continue

        content = doc.page_content or ""
        chunk_codes = extract_course_codes(content)
        hit_codes = sorted(chunk_codes.intersection(gold_set))
        predicted_codes.update(chunk_codes)

        if hit_codes and first_relevant_rank is None:
            first_relevant_rank = idx

        retrieved_chunks.append(
            {
                "rank": idx,
                "score": score,
                "source": source,
                "parent_id": doc.metadata.get("parent_id", ""),
                "codes_in_chunk": sorted(chunk_codes),
                "matched_gold_codes": hit_codes,
            }
        )

    true_positive = len(predicted_codes.intersection(gold_set))
    precision = true_positive / len(predicted_codes) if predicted_codes else 0.0
    recall = true_positive / len(gold_set) if gold_set else 0.0
    f1 = (2 * precision * recall / (precision + recall)) if (precision + recall) else 0.0
    mrr = (1.0 / first_relevant_rank) if first_relevant_rank else 0.0

    metrics = {
        "query": query,
        "top_k": top_k,
        "source_filter": source_filter or "",
        "gold_count": len(gold_set),
        "predicted_code_count": len(predicted_codes),
        "true_positive": true_positive,
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "f1": round(f1, 4),
        "mrr": round(mrr, 4),
        "missed_gold_codes": sorted(gold_set.difference(predicted_codes)),
        "hit_gold_codes": sorted(gold_set.intersection(predicted_codes)),
    }
    return metrics, retrieved_chunks


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Minimal retrieval evaluator for this RAG project."
    )
    parser.add_argument(
        "--query",
        type=str,
        default=DEFAULT_SAMPLE["query"],
        help="Evaluation query.",
    )
    parser.add_argument(
        "--gold-codes",
        type=str,
        default=",".join(DEFAULT_SAMPLE["gold_codes"]),
        help="Comma-separated gold course codes.",
    )
    parser.add_argument(
        "--top-k",
        type=int,
        default=8,
        help="Number of retrieved chunks.",
    )
    parser.add_argument(
        "--source",
        type=str,
        default=DEFAULT_SAMPLE["source"],
        help="Optional source filename filter, e.g. 电子信息培养方案.pdf",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    gold_codes = [normalize_code(item) for item in args.gold_codes.split(",") if item.strip()]

    metrics, chunks = evaluate_retrieval(
        query=args.query,
        gold_codes=gold_codes,
        top_k=args.top_k,
        source_filter=args.source or None,
    )

    print("=== Retrieval Metrics ===")
    print(json.dumps(metrics, ensure_ascii=False, indent=2))

    print("\n=== Retrieved Chunks (rank + matched_gold_codes) ===")
    for item in chunks:
        score = item["score"]
        score_text = f"{score:.6f}" if isinstance(score, (float, int)) else "N/A"
        print(
            f"rank={item['rank']}, score={score_text}, source={item['source']}, "
            f"matched={item['matched_gold_codes']}"
        )


if __name__ == "__main__":
    main()
