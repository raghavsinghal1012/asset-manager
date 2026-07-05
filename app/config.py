from pathlib import Path

# -------------------------
# Project Paths
# -------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

UPLOAD_FOLDER = BASE_DIR / "uploads"
GENERATED_FOLDER = BASE_DIR / "generated"
DATABASE_PATH = BASE_DIR / "database" / "assets.db"

# -------------------------
# Company
# -------------------------

COMPANY_NAME = "Firm 1"

# -------------------------
# Database Backend
# -------------------------

DATABASE_BACKEND = "postgres"      # "sqlite" or "postgres"

SQLITE_DATABASE_URL = f"sqlite:///{DATABASE_PATH}"

POSTGRES_DATABASE_URL = (
    "postgresql://postgres:UNtEimvPDEiMdbtNEVgUfMRFYSYHqUKu@hayabusa.proxy.rlwy.net:10548/railway"
)

if DATABASE_BACKEND == "postgres":
    DATABASE_URL = POSTGRES_DATABASE_URL
else:
    DATABASE_URL = SQLITE_DATABASE_URL

# -------------------------
# Public URL
# -------------------------

BASE_URL = "http://127.0.0.1:8000"