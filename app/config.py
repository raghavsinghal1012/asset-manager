from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_PATH = BASE_DIR / "database" / "assets.db"

UPLOAD_FOLDER = BASE_DIR / "uploads"

COMPANY_NAME = "Firm 1"