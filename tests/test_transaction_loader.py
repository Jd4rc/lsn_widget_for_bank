import json
from idlelib.iomenu import encoding
from unittest.mock import patch

import pandas as pd
import pytest

from src.utils import load_transactions


def test_load_transactions_with_happy_path(tmp_path, monkeypatch):
    data_dir = tmp_path / "data"
    data_dir.mkdir()

    file_path = data_dir / "operations.json"

    data = [
        {"id": 1},
        {"id": 2},
    ]

    file_path.write_text(
        json.dumps(data),
        encoding="utf-8",
    )

    monkeypatch.setattr(
        "src.utils.BASE_DIR", tmp_path
    )

    result = load_transactions("data/operations.json")

    assert result == data



def test_load_transactions_with_empty_data(
        tmp_path, monkeypatch
):
    data_dir = tmp_path / "data"
    data_dir.mkdir()

    file_path = data_dir / "operations.json"


    file_path.write_text(
        '[]',
        encoding="utf-8",
    )

    monkeypatch.setattr(
        "src.utils.BASE_DIR",
        tmp_path
    )

    result = load_transactions("data/operations.json")

    assert result == []



def test_load_transactions_with_custom_path(tmp_path, monkeypatch):
    data_dir = tmp_path / "data"
    data_dir.mkdir()

    file_path = data_dir / "test.json"

    data = [
        {"id": 1},
        {"id": 2}
    ]

    file_path.write_text(
        json.dumps(data),
        encoding="utf-8",
    )

    monkeypatch.setattr(
        "src.utils.BASE_DIR",
        tmp_path
    )



    result = load_transactions("data/test.json")

    assert result == [{"id": 1}, {"id": 2}]


def test_load_transactions_with_invalid_json(tmp_path, monkeypatch):
    data_dir = tmp_path / 'data'
    data_dir.mkdir()

    file_path = data_dir / 'test.json'

    file_path.write_text(
        "invalid json",
        encoding="utf-8",
    )

    monkeypatch.setattr(
        "src.utils.BASE_DIR",
        tmp_path
    )


    result = load_transactions("data/test.json")

    assert result == []


def test_load_transactions_with_file_not_found(tmp_path, monkeypatch):
    monkeypatch.setattr(
        "src.utils.BASE_DIR",
        tmp_path
    )

    result = load_transactions("data/operation.json")

    assert result == []


def test_load_transaction_from_csv(
        tmp_path,
        monkeypatch,
):
    data_dir = tmp_path / 'data'
    data_dir.mkdir()

    file_path = data_dir / "operations.csv"

    file_path.write_text(
        'id,amount,currency\n1,100,RUB\n2,200,USD\n',
        encoding="utf-8",
    )

    monkeypatch.setattr(
        'src.utils.BASE_DIR',
        tmp_path
    )

    result = load_transactions("data/operations.csv")

    assert result == [
        {"id": '1', "amount": '100', "currency": "RUB"},
        {"id": '2', "amount": '200', "currency": "USD"},
    ]


def test_load_transaction_from_xlsx(
        tmp_path,
        monkeypatch
):
    data_dir = tmp_path / 'data'
    data_dir.mkdir()

    file_path = data_dir / "operations.xlsx"

    dataframe = pd.DataFrame(
        [
            {"id": 1, "amount": 100, "currency": "RUB"},
            {"id": 2, "amount": 200, "currency": "USD"},
        ]
    )

    dataframe.to_excel(
        file_path,
        index=False,
    )


    monkeypatch.setattr(
        'src.utils.BASE_DIR',
        tmp_path
    )

    result = load_transactions("data/operations.xlsx")

    assert result == [
        {"id": 1, "amount": 100, "currency": "RUB"},
        {"id": 2, "amount": 200, "currency": "USD"},
    ]