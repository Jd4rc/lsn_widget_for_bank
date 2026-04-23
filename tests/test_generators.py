from src.generators import filter_by_currency, transaction_descriptions


def test_filter_by_currency(base_transactions_in,base_transactions_out_1, base_transactions_out_2, base_transactions_out_3):
    i = filter_by_currency(base_transactions_in, "USD")
    assert next(i) == base_transactions_out_1
    assert next(i) == base_transactions_out_2
    assert next(i) == base_transactions_out_3



def test_transaction_descriptions(base_transactions_in, base_descriptions_out_1, base_descriptions_out_2, base_descriptions_out_3):
    i = transaction_descriptions(base_transactions_in)
    assert next(i) == base_descriptions_out_1
    assert next(i) == base_descriptions_out_2
    assert next(i) == base_descriptions_out_3