import json
from unittest.mock import patch

import pytest

from src.utils.transaction_loader import load_transactions


@patch("src.utils.transaction_loader.Path.read_text")
def test_load_transactions_with_happy_path(mock_read_text):
    data = [
        {"id": 1},
        {"id": 2},
    ]

    mock_read_text.return_value = json.dumps(data)

    result = load_transactions("data/operations.json")

    assert result == data

    mock_read_text.assert_called_with(encoding="utf-8")


@patch("src.utils.transaction_loader.Path.read_text")
def test_load_transactions_with_empty_data(mock_read_text):
    data: list[dict[str, str | int]] = []

    mock_read_text.return_value = json.dumps(data)

    result = load_transactions("data/operations.json")

    assert result == []

    mock_read_text.assert_called_with(encoding="utf-8")


@patch("src.utils.transaction_loader.Path.read_text")
def test_load_transactions_with_custom_path(mock_read_text):
    mock_read_text.return_value = '[{"id": 1},{"id": 2}]'

    result = load_transactions("data/test.json")

    assert result == [{"id": 1}, {"id": 2}]


@patch("src.utils.transaction_loader.Path.read_text")
def test_load_transactions_with_invalid_json(mock_read_text):
    mock_read_text.return_value = "invalid json"

    with pytest.raises(json.JSONDecodeError):
        load_transactions("data/operations.json")


@patch("src.utils.transaction_loader.Path.read_text")
def test_load_transactions_with_file_not_found(mock_read_text):
    mock_read_text.side_effect = FileNotFoundError

    with pytest.raises(FileNotFoundError):
        load_transactions("data/operations.json")
