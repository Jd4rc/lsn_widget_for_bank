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


    url = "https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from}&amount={amount}"

    payload = {}
    headers = {
        "apikey": EXCHANGE_RATES_API_KEY
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code
    result = response.text