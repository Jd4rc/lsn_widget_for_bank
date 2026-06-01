from pathlib import Path
import json


BASE_DIR = Path(__file__).resolve().parent.parent.parent

def load_transactions(
        filepath: str
) -> list[dict]:
    file_path = Path(BASE_DIR / filepath)

    transactions = json.loads(
        file_path.read_text(
            encoding="utf-8"
        )
    )
    return transactions
