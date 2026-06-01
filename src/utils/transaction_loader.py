from typing import Any
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent


def load_transactions(filepath: str) -> list[dict[str, Any]]:
    """
    Читает JSON-файл и преобразует его содержимое
    в список словарей с данными транзакций.

    :param filepath: Относительный путь к файлу с транзакциями.
    :return: Список транзакций.
    :raises FileNotFoundError: Если указанный файл не найден.
    :raises json.JSONDecodeError: Если файл содержит некорректный JSON.
    """
    file_path = Path(BASE_DIR / filepath)

    transactions = json.loads(file_path.read_text(encoding="utf-8"))
    return transactions
