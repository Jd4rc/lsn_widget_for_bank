import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "app.log"

logging.basicConfig(
    level=logging.INFO,
    format=("%(asctime)s - " "%(name)s - " "%(levelname)s - " "%(message)s"),
    filename=LOG_FILE,
    filemode="w",
    encoding="utf-8",
)
