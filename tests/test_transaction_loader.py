import json
from unittest.mock import patch

from src.utils.transaction_loader import load_transactions

@patch('src.utils.transaction_loader.Path.read_text')
def test_load_transactions_with_happy_path(mock_read_text):
    data = [
        {"id": 1},
        {"id": 2},
    ]

    mock_read_text.return_value = json.dumps(data)

    result = load_transactions('data/operations.json')

    assert result == data

    mock_read_text.assert_called_with(
        encoding="utf-8"
    )


@patch('src.utils.transaction_loader.Path.read_text')
def test_load_transactions_with_empty_data(mock_read_text):
    data = []

    mock_read_text.return_value = json.dumps(data)

    result = load_transactions('data/operations.json')

    assert result == []

    mock_read_text.assert_called_with(
        encoding="utf-8"
    )