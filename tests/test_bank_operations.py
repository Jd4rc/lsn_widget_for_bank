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

def test_process_bank_operations_counts_categories():
    data = [
        {"description": "Перевод организации"},
        {"description": "Перевод с карты на карту"},
        {"description": "Открытие вклада"},
        {"description": "Перевод со счета на счет"},
    ]

    categories = [
        'Открытие'
    ]
    result = process_bank_operations(data, categories)

    assert result == {
            "Открытие": 1
        }

def test_process_bank_operations_returns_zero_for_missing_category():
    data = [
        {"description": "Перевод организации"},
        {"description": "Открытие вклада"},
    ]

    categories = ["Перевод", "Снятие наличных"]

    result = process_bank_operations(data, categories)

    assert result == {
        "Перевод": 1,
        "Снятие наличных": 0,
    }

def test_process_bank_operations_ignore_case():
    data = [
        {"description": "перевод организации"},
        {"description": "ПЕРЕВОД с карты на карту"},
        {"description": "Открытие вклада"},
    ]

    categories = ["Перевод"]

    result = process_bank_operations(data, categories)

    assert result == {
        "Перевод": 2,
    }