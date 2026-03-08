from datetime import datetime
from src.core.Config import Config
from pathlib import Path

class Logger:
    LOG_FILE = Path("logs.txt")
    def __init__(self) -> None:
        pass

    @classmethod
    def _now(cls):
        return datetime.now().strftime(Config.DATE_FORMAT)
    
    @classmethod
    def write(cls, text: str, alsoInConsole: bool = False):
        line = f"{cls._now()} | {text}\n"

        cls.LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

        with open(cls.LOG_FILE, "a", encoding="utf-8") as f:
            f.write(line)

        if alsoInConsole:
            print(line, end="")

    @classmethod
    def info(cls, text: str, alsoInConsole: bool = False):
        cls.write(f"INFO - {text}", alsoInConsole)
    
    @classmethod
    def warn(cls, text: str, alsoInConsole: bool = False):
        cls.write(f"WARN - {text}", alsoInConsole)

    @classmethod
    def error(cls, text: str, alsoInConsole: bool = False):
        cls.write(f"ERROR - {text}", alsoInConsole)
    
    @classmethod
    def critical(cls, text: str, alsoInConsole: bool = False):
        cls.write(f"CRITICAL - {text}", alsoInConsole)
    
    @classmethod
    def debug(cls, text: str, alsoInConsole: bool = False):
        cls.write(f"DEBUG - {text}", alsoInConsole)