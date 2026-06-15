from src.processing import process_bank_operations
from src.processing import process_bank_search


def test_process_bank_search_found_transactions():
    data = [
        {"description": "Перевод организации"},
        {"description": "Открытие вклада"},
        {"description": "Перевод с карты на карту"},
    ]

    result = process_bank_search(data, "перевод")

    assert result == [
        {"description": "Перевод организации"},
        {"description": "Перевод с карты на карту"},
    ]

def test_process_bank_search_ignore_case():
    data = [
        {"description": "Перевод организации"},
        {"description": "Открытие вклада"},
    ]

    result = process_bank_search(data, "ПЕРЕВОД")

    assert result == [
        {"description": "Перевод организации"},
    ]

def test_process_bank_search_not_found():
    data = [
        {"description": "Перевод организации"},
        {"description": "Открытие вклада"},
    ]

    result = process_bank_search(data, "магазин")

    assert result == []
