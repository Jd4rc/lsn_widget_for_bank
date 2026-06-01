from unittest.mock import patch
import pytest
from src.utils.external_api import get_transaction_amount

def test_get_transaction_amount_with_rub():
    transaction = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }

    result = get_transaction_amount(transaction)

    assert result == 31957.58

@patch('src.utils.external_api.requests.get')
def test_get_transaction_amount_with_no_rub(mock_get):
    transaction = {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    }

    mock_response = mock_get.return_value
    mock_response.json.return_value = {'result': 12300.1411}

    result = get_transaction_amount(transaction)

    assert result == 12300.1411
    mock_response.raise_for_status.assert_called_once()

@patch('src.utils.external_api.requests.get')
def test_get_transaction_amount_with_unsupported_currency(mock_get):
    transaction = {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "Afghani",
                "code": "AFN"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    }

    with pytest.raises(ValueError):
        get_transaction_amount(transaction)


    mock_get.assert_not_called()


