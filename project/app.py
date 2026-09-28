import sys
import os
import logging

sys.path.insert(0, os.path.dirname(__file__))
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# Ensure localhost calls used by Gradio startup checks bypass proxies.
_no_proxy_entries = {"127.0.0.1", "localhost"}
for _key in ("NO_PROXY", "no_proxy"):
    _current = os.environ.get(_key, "")
    _parts = {p.strip() for p in _current.split(",") if p.strip()}
    _parts.update(_no_proxy_entries)
    os.environ[_key] = ",".join(sorted(_parts))

from dotenv import load_dotenv
load_dotenv(os.path.join(os.path.dirname(__file__), ".env"), override=True)

# Keep the same HuggingFace model workflow, but use an accessible endpoint in restricted networks.
os.environ.setdefault("HF_ENDPOINT", "https://huggingface.co")
os.environ.setdefault("HF_HUB_ETAG_TIMEOUT", "60")
os.environ.setdefault("HF_HUB_DOWNLOAD_TIMEOUT", "120")

# Suppress OTel "Failed to detach context" warning caused by generator/context interaction.
# Tracing is unaffected.
# Known bug: https://github.com/open-telemetry/opentelemetry-python/issues/2606
class _SuppressOtelDetachWarning(logging.Filter):
    def filter(self, record):
        return "Failed to detach context" not in record.getMessage()

logging.getLogger("opentelemetry.context").addFilter(_SuppressOtelDetachWarning())

from ui.css import custom_css
from ui.gradio_app import create_gradio_ui

if __name__ == "__main__":
    print("\n🔨 Creating RAG Assistant...")
    demo = create_gradio_ui()
    print("\n🚀 Launching RAG Assistant...")
    demo.launch(css=custom_css, server_name="127.0.0.1")

