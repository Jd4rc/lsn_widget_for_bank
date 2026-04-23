from src.generators import filter_by_currency


def test_filter_by_currency_with_out_1(base_transactions_in, base_transactions_out_1):
    assert next(filter_by_currency(base_transactions_in, 'USD')) == base_transactions_out_1

def test_filter_by_currency_with_out_2(base_transactions_in, base_transactions_out_2):
    assert next(filter_by_currency(base_transactions_in, 'USD')) == base_transactions_out_2


def test_filter_by_currency_with_out_3(base_transactions_in, base_transactions_out_3):
    assert next(filter_by_currency(base_transactions_in, 'USD')) == base_transactions_out_3