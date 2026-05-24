import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

ROOT = Path(__file__).resolve().parents[1]
DOCS_DIRS = [ROOT / "docs" / "playbook", ROOT / "docs" / "handbook"]
CHROMA_PATH = ROOT / "data" / "chroma"
COLLECTION_NAME = "job_copilot"

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
CHAT_MODEL = os.getenv("OPENAI_CHAT_MODEL", "gpt-4o-mini")
EMBED_MODEL = os.getenv("OPENAI_EMBED_MODEL", "text-embedding-3-small")
TOP_K = int(os.getenv("TOP_K", "5"))
