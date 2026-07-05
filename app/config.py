import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

UPLOAD_FOLDER = BASE_DIR / "uploads"
GENERATED_FOLDER = BASE_DIR / "generated"
DATABASE_PATH = BASE_DIR / "database" / "assets.db"

COMPANY_NAME = "Firm 1"

DATABASE_BACKEND = os.getenv("DATABASE_BACKEND", "postgres")

SQLITE_DATABASE_URL = f"sqlite:///{DATABASE_PATH}"

POSTGRES_DATABASE_URL = os.getenv("DATABASE_URL")

DATABASE_URL = (
    POSTGRES_DATABASE_URL
    if DATABASE_BACKEND == "postgres"
    else SQLITE_DATABASE_URL
)

BASE_URL = os.getenv(
    "BASE_URL",
    "http://127.0.0.1:8000"
)