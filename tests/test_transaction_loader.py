import json
from unittest.mock import patch

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
