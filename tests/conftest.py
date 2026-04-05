import pytest

@pytest.fixture
def base_card_number_1():
    return 7000792289606361

@pytest.fixture
def base_card_number_2():
    return 7000792289606591

@pytest.fixture
def base_card_number_3():
    return 7000792289606123


@pytest.fixture
def base_account_number_1():
    return 73654108430135874305

@pytest.fixture
def base_account_number_2():
    return 73654108430135874123

@pytest.fixture
def base_account_number_3():
    return 73654108430135874789

@pytest.fixture
def base_mask_account_1():
    return 'Счет 73654108430135874305'

@pytest.fixture
def base_mask_account_2():
    return 'Счет не мой 73654108430135871505'

@pytest.fixture
def base_mask_account_3():
    return 'Счет Олега 73654108430135870195'

@pytest.fixture
def base_mask_account_4():
    return 'Maestro 7000792289609184'

@pytest.fixture
def base_mask_account_5():
    return 'Visa Platinum 7000792289609854'

@pytest.fixture
def base_mask_account_6():
    return 'Visa 7000792289609854'



