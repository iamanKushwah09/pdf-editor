from pathlib import Path

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Storage directories
STORAGE_DIR = BASE_DIR / "storage"
UPLOAD_DIR = STORAGE_DIR / "uploads"
PAGES_DIR = STORAGE_DIR / "pages"
OUTPUT_DIR = STORAGE_DIR / "outputs"

# Create directories if not exist
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
PAGES_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Upload limits
ALLOWED_EXTENSIONS = {".pdf"}
MAX_FILE_SIZE_MB = 50
