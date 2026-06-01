import requests



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
        "apikey": API_KEY
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code
    result = response.text