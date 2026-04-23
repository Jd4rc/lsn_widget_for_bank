from src.generators import filter_by_currency


def test_filter_by_currency(base_transactions_in, base_transactions_out_1, base_transactions_out_2, base_transactions_out_3):
    generator = filter_by_currency(base_transactions_in, 'USD')
    assert next(generator) == base_transactions_out_1
    assert next(generator) == base_transactions_out_2
    assert next(generator) == base_transactions_out_3
