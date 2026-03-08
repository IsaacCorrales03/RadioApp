from pathlib import Path

class Config:
    BASE_DIR = Path(__file__).resolve().parent.parent
    LOG_DIR = BASE_DIR / "logs"
    LOG_FILE = LOG_DIR / "system.log"
    DATE_FORMAT = "%Y-%m-%d"
    DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"