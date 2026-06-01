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
    amount = float(transaction['operationAmount']['amount'])
    currency = transaction['operationAmount']['currency']['code']

    if currency == 'RUB':
        return float(amount)

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