import pytest
from src.widget import mask_account_card, get_date

def test_mask_account_card_with_base_1(base_mask_account_1):
    assert mask_account_card(base_mask_account_1) == 'Счет **4305'

def test_mask_account_card_with_base_2(base_mask_account_2):
    assert mask_account_card(base_mask_account_2) == 'Счет не мой **1505'

def test_mask_account_card_with_base_3(base_mask_account_3):
    assert mask_account_card(base_mask_account_3) == 'Счет Олега **0195'

def test_mask_account_card_with_base_4(base_mask_account_4):
    assert mask_account_card(base_mask_account_4) == 'Maestro 7000 79** **** 9184'

def test_mask_account_card_with_base_5(base_mask_account_5):
    assert mask_account_card(base_mask_account_5) == 'Visa Platinum 7000 79** **** 9854'

def test_mask_account_card_with_base_6(base_mask_account_6):
    assert mask_account_card(base_mask_account_6) == 'Visa 7000 79** **** 9854'

@pytest.mark.parametrize('mask_account, expected', [
    ('', ValueError),
    (123, TypeError),
    (True, TypeError),
    ('Счет 123 73654108430135870195', ValueError),
    ('Maestro 123 7000792289609184', ValueError)
])
def test_mask_account_card_with_invalid_data_parametrized(mask_account, expected):
    with pytest.raises(expected):
        mask_account_card(mask_account)

def test_get_date_with_base_1(base_date_1):
    assert get_date(base_date_1)

def test_get_date_with_base_2(base_date_2):
    assert get_date(base_date_2)

def test_get_date_with_base_3(base_date_3):
    assert get_date(base_date_3)

@pytest.mark.parametrize('date_str, expected', [
    ('', ValueError),
    (123, TypeError),
    (True, TypeError),
    (None, TypeError),
    ('2022-07-11', ValueError),
    ('Maestro 2022-07-11', ValueError),
    ('2022.07.11', ValueError),
    ([1, 2, 3], TypeError)
])
def test_get_date_with_invalid_data_parametrized(date_str, expected):
    with pytest.raises(expected):
        get_date(date_str)