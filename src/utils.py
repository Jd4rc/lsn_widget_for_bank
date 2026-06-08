import json
import logging
import os
from pathlib import Path
from typing import Any

import requests
from dotenv import load_dotenv

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

    logger.info("Processing transaction amount")

    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]

    logger.debug(
        "Transaction amount=%s currency=%s",
        amount,
        currency,
    )

    if currency == "RUB":
        logger.info("Currency is RUB, conversion not required")
        return amount

    if currency not in ("EUR", "USD"):
        logger.error("Unsupported currency: %s", currency)
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

    logger.info("Sending request to exchange rates API")

    response = requests.get(url, headers=headers, params=params)

    response.raise_for_status()

    logger.info("Exchange rates API request successful")

    data = response.json()

    result = float(data["result"])

    logger.info(
        "Converted %.2f %s to %.2f RUB",
        amount,
        currency,
        result,
    )

    return result


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

    logger.info("Loading transactions from %s", filepath)

    try:
        transactions = json.loads(file_path.read_text(encoding="utf-8"))

        logger.info("Successfully loaded transactions file")

        if not isinstance(transactions, list):
            logger.warning("Transactions data is not a list")
            return []

        logger.info("Loaded %s transactions", len(transactions))
        return transactions

    except json.decoder.JSONDecodeError:
        logger.error("Invalid JSON in file %s", filepath)
        return []
