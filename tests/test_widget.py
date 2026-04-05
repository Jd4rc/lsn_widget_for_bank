import pytest
from src.widget import mask_account_card

def test_mask_account_card_with_base_1(base_mask_account_1):
    assert mask_account_card(base_mask_account_1)

def test_mask_account_card_with_base_2(base_mask_account_2):
    assert mask_account_card(base_mask_account_2)

def test_mask_account_card_with_base_3(base_mask_account_3):
    assert mask_account_card(base_mask_account_3)

def test_mask_account_card_with_base_4(base_mask_account_4):
    assert mask_account_card(base_mask_account_4)

def test_mask_account_card_with_base_5(base_mask_account_5):
    assert mask_account_card(base_mask_account_5)

def test_mask_account_card_with_base_6(base_mask_account_6):
    assert mask_account_card(base_mask_account_6)

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