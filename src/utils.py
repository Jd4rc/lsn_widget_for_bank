from typing import Any
import json
from pathlib import Path
import os
import requests
from dotenv import load_dotenv
import logging

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")
EXCHANGE_RATES_API_KEY = os.getenv("EXCHANGE_RATES_API_KEY")


def get_transaction_amount(
    transaction: dict,
) -> float:
    """
    Извлекает сумму и валюту из транзакции и возвращает сумму в рублях.

    Поддерживаются валюты RUB, USD и EUR. Для USD и EUR выполняется
    конвертация через внешний сервис обменных курсов.

    :param transaction: Словарь транзакции, содержащий ключи
        operationAmount.amount и operationAmount.currency.code.
    :return: Сумма транзакции в RUB.
    :raises ValueError: Если валюта не является RUB, USD или EUR.
    :raises requests.RequestException: При ошибке HTTP-запроса.
    """
    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return amount

    if currency not in ("EUR", "USD"):
        raise ValueError("Currency must be RUB or EUR or USD")

    url = "https://api.apilayer.com/exchangerates_data/convert"

    if EXCHANGE_RATES_API_KEY is None:
        raise ValueError("EXCHANGE_RATES_API_KEY not set")

    headers = {"apikey": EXCHANGE_RATES_API_KEY}

    params = {
        "to": "RUB",
        "from": currency,
        "amount": amount,
    }

    response = requests.get(url, headers=headers, params=params)

    response.raise_for_status()

    data = response.json()

    return float(data["result"])


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

    try:
        transactions = json.loads(file_path.read_text(encoding="utf-8"))

        if not isinstance(transactions, list):
            return []

        return transactions
    except json.decoder.JSONDecodeError:
        return []
