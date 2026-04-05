import pytest
from src.masks import get_mask_account
from src.masks import get_mask_card_number

def test_get_mask_card_number_with_base_card_number_1(base_card_number_1):
    assert get_mask_card_number(base_card_number_1) == '7000 79** **** 6361'

def test_get_mask_card_number_with_base_card_number_2(base_card_number_2):
    assert get_mask_card_number(base_card_number_2) == '7000 79** **** 6591'

def test_get_mask_card_number_with_base_card_number_3(base_card_number_3):
    assert get_mask_card_number(base_card_number_3) == '7000 79** **** 6123'

def test_get_mask_account_with_base_account_number_1(base_account_number_1):
    assert get_mask_account(base_account_number_1) == '**4305'

def test_get_mask_account_with_base_account_number_2(base_account_number_2):
    assert get_mask_account(base_account_number_2) == '**4123'

def test_get_mask_account_with_base_account_number_3(base_account_number_3):
    assert get_mask_account(base_account_number_3) == '**4789'

@pytest.mark.parametrize('card_number, expected', [
    (1234567, ValueError),
    (890101, ValueError),
    ('Hello World', TypeError),
    ('qqqqqqqqqqqqqqqq', TypeError),
    ('', TypeError)
])
def test_get_mask_card_number_with_invalid_data_parametrized(card_number, expected):
    with pytest.raises(expected):
        get_mask_card_number(card_number)

@pytest.mark.parametrize('account_number, expected', [
    (12345678905639856794, '**6794'),
    (82859175819692817685, '**7685'),
    (95827576819572856728, '**6728'),
    (91857271859819598195, '**8195'),
    (12516264296923569023, '**9023')
])
def test_get_mask_account_with_correct_data_parametrized(account_number, expected):
    assert get_mask_account(account_number) == expected

@pytest.mark.parametrize('account_number, expected', [
    (748184124, ValueError),
    (881, ValueError),
    ('123', ValueError),
    (81283481248912984912491294, ValueError),
    ('qegfqgqegeqgegwegwe', TypeError),
    ('', TypeError),
    (True, TypeError),

])
def test_get_mask_account_with_invalid_data_parametrized(account_number, expected):
    with pytest.raises(expected):
        get_mask_account(account_number)

