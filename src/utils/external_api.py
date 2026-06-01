from dotenv import load_dotenv
from pathlib import Path
import os
import requests

BASE_DIR = Path(__file__).resolve().parent.parent.parent

load_dotenv(BASE_DIR / '.env')
EXCHANGE_RATES_API_KEY = os.getenv('EXCHANGE_RATES_API_KEY')


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
    amount = float(transaction['operationAmount']['amount'])
    currency = transaction['operationAmount']['currency']['code']

    if currency == 'RUB':
        return amount

    if currency not in ('EUR', 'USD'):
        raise ValueError(
            'Currency must be RUB or EUR or USD'
        )


    url = "https://api.apilayer.com/exchangerates_data/convert"

    headers = {
        "apikey": EXCHANGE_RATES_API_KEY
    }

    params = {
        "to": 'RUB',
        "from": currency,
        "amount": amount,
    }

    response = requests.get(
        url,
        headers=headers,
        params=params
    )

    response.raise_for_status()

    data = response.json()


    return data['result']