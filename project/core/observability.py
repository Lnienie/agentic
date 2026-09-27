import logging
import config

logger = logging.getLogger(__name__)


class Observability:

    def __init__(self):
        self._enabled = config.LANGFUSE_ENABLED
        self._handler = None
        self._client = None

        if not self._enabled:
            return

        if not config.LANGFUSE_PUBLIC_KEY or not config.LANGFUSE_SECRET_KEY:
            logger.warning("Langfuse enabled but API keys are missing — skipping")
            self._enabled = False
            return

        try:
            from langfuse import Langfuse
            from langfuse.langchain import CallbackHandler

            import os
            os.environ["LANGFUSE_PUBLIC_KEY"] = config.LANGFUSE_PUBLIC_KEY
            os.environ["LANGFUSE_SECRET_KEY"] = config.LANGFUSE_SECRET_KEY
            os.environ["LANGFUSE_HOST"] = config.LANGFUSE_BASE_URL

            self._client = Langfuse()

            if self._client.auth_check():
                print("Langfuse client is authenticated and ready!")
            else:
                print("Authentication failed. Please check your credentials and host.")
                self._enabled = False
                return

            self._handler = CallbackHandler()
        except Exception as exc:
            logger.warning("Could not initialize Langfuse: %s", exc)
            self._enabled = False

    def get_handler(self):
        return self._handler

    def flush(self):
        if self._client is not None:
            try:
                self._client.flush()
            except Exception:
                pass