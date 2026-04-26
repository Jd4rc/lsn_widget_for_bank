from logging import raiseExceptions

import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency_with_usd(base_transactions_in,base_transactions_out_1, base_transactions_out_2, base_transactions_out_3):
    i = filter_by_currency(base_transactions_in, "USD")
    assert next(i) == base_transactions_out_1
    assert next(i) == base_transactions_out_2
    assert next(i) == base_transactions_out_3


def test_filter_by_currency_with_rub(base_transactions_in, base_transactions_out_4, base_transactions_out_5):
    i = filter_by_currency(base_transactions_in, "RUB")
    assert next(i) == base_transactions_out_4
    assert next(i) == base_transactions_out_5

def test_filter_by_currency_with_missing_currency(base_transactions_in):
    i = filter_by_currency(base_transactions_in, "CNY")
    with pytest.raises(StopIteration):
        next(i)

def test_filter_by_currency_without_currency(base_transactions_in_without_currency):
    with pytest.raises(KeyError):
        i = filter_by_currency(base_transactions_in_without_currency, "RUB")

        next(i)

def test_filter_by_currency_with_another_type_of_data(base_transactions_in_another_type_of_data):
    i = filter_by_currency(base_transactions_in_another_type_of_data, "USD")

    with pytest.raises(TypeError):
        next(i)
def test_filter_by_currency_with_another_type_of_data_el(base_transactions_in_another_type_of_data_el):
    with pytest.raises(TypeError):
        i = filter_by_currency(base_transactions_in_another_type_of_data_el, "RUB")

        next(i)


def test_transaction_descriptions(base_transactions_in, base_descriptions_out_1, base_descriptions_out_2, base_descriptions_out_3):
    i = transaction_descriptions(base_transactions_in)
    assert next(i) == base_descriptions_out_1
    assert next(i) == base_descriptions_out_2
    assert next(i) == base_descriptions_out_3

def test_transaction_without_descriptions(base_transactions_in_without_descriptions):
    with pytest.raises(KeyError):
        i = transaction_descriptions(base_transactions_in_without_descriptions)

        next(i)


@pytest.mark.parametrize("start, end, expected, error", [ # смешал чистый с ловлей ошибки, чтобы попробовать
    (1, 5,
     ["0000 0000 0000 0001",
     "0000 0000 0000 0002",
     "0000 0000 0000 0003",
     "0000 0000 0000 0004",
     "0000 0000 0000 0005",],
     None),
    (2, 10,
     ["0000 0000 0000 0002",
      "0000 0000 0000 0003",
      "0000 0000 0000 0004",
      "0000 0000 0000 0005",
      "0000 0000 0000 0006",
      "0000 0000 0000 0007",
      "0000 0000 0000 0008",
      "0000 0000 0000 0009",
      "0000 0000 0000 0010"],
     None),
    (10000, 10005,
     ["0000 0000 0001 0000",
      "0000 0000 0001 0001",
      "0000 0000 0001 0002",
      "0000 0000 0001 0003",
      "0000 0000 0001 0004",
      "0000 0000 0001 0005",],
     None),
    (10, 0, None, ValueError)
])

def test_card_number_generator(start, end, expected, error):
    if error:
        with pytest.raises(ValueError):
            [card_number for card_number in card_number_generator(start, end)]
    else:
        assert [card_number for card_number in card_number_generator(start, end)] == expected