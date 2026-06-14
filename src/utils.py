import csv
import json
import logging
import os
from pathlib import Path
from typing import Any, cast

import pandas as pd
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

    logger.info(
        "Transaction amount=%s currency=%s",
        amount,
        currency,
    )

    if currency == "RUB":
        logger.info(
            "Currency is RUB, conversion not required Amount=%s RUB",
            amount,
        )
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


def _load_json(file_path: Path) -> list[dict[str, Any]]:
    with open(file_path, encoding="utf-8") as f:

        data = json.load(f)

        return cast(
            list[dict[str, Any]],
            data,
        )


def _load_csv(file_path: Path) -> list[dict[str, Any]]:
    with open(file_path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def _load_xlsx(file_path: Path) -> list[dict[str, Any]]:
    dataframe = pd.read_excel(file_path)

    transactions = dataframe.to_dict(
        orient="records"
    )

    return cast(
        list[dict[str, Any]],
        transactions,
    )


def load_transactions(filepath: str) -> list[dict[str, Any]]:
    """
    Загружает транзакции из JSON, CSV или XLSX файла.


    :param filepath: Относительный путь к файлу с транзакциями.
    :return: Список транзакций.
    :raises FileNotFoundError: Если указанный файл не найден.
    :raises json.JSONDecodeError: Если файл содержит некорректный JSON.
    """
    file_path = Path(BASE_DIR / filepath)

    logger.info("Loading transactions from %s", filepath)

    try:
        if file_path.suffix == ".json":
            transactions = _load_json(file_path)

        elif file_path.suffix == ".csv":
            transactions = _load_csv(file_path)

        elif file_path.suffix == ".xlsx":
            transactions = _load_xlsx(file_path)

        else:
            logger.error(
                "Unsupported file format: %s",
                file_path.suffix,
            )

            return []

        logger.info("Loaded %s transactions", len(transactions))
        return transactions

    except FileNotFoundError:
        logger.error(
            "File not found: %s",
            filepath,
        )
        return []

    except json.decoder.JSONDecodeError:
        logger.error("Invalid JSON in file %s", filepath)
        return []

    except Exception as error:
        logger.error(
            "Error loading transactions: %s",
            error,
        )
        return []
