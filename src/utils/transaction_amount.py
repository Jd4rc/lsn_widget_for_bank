from dotenv import load_dotenv
from pathlib import Path
import os
import requests

BASE_DIR = Path(__file__).resolve().parent.parent.parent

load_dotenv(BASE_DIR / '.env')
EXCHANGE_RATES_API_KEY = os.getenv('Exchange_Rates_Data_API')


def get_transaction_amount(
        transaction: dict,
) -> float:
    amount = transaction['operationAmount']['amount']
    currency = transaction['operationAmount']['currency']['code']

    if currency == 'RUB':
        return amount


    url = "https://api.apilayer.com/exchangerates_data/convert"

    headers = {
        "apikey": EXCHANGE_RATES_API_KEY
    }

    if currency == 'USD':
        params = {
            "to": 'RUB',
            "from": 'USD',
            "amount": amount,
        }

    if currency == 'EUR':
        params = {
            "to": 'RUB',
            "from": 'EUR',
            "amount": amount,
        }


    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    response = response.json()