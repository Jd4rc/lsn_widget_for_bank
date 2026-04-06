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
    return "Счет 73654108430135874305"


@pytest.fixture
def base_mask_account_2():
    return "Счет не мой 73654108430135871505"


@pytest.fixture
def base_mask_account_3():
    return "Счет Олега 73654108430135870195"


@pytest.fixture
def base_mask_account_4():
    return "Maestro 7000792289609184"


@pytest.fixture
def base_mask_account_5():
    return "Visa Platinum 7000792289609854"


@pytest.fixture
def base_mask_account_6():
    return "Visa 7000792289609854"


@pytest.fixture
def base_date_1():
    return "2024-03-11T02:26:18.671407"


@pytest.fixture
def base_date_2():
    return "2022-07-11T03:26:18.671407"


@pytest.fixture
def base_date_3():
    return "2021-01-02T02:26:18.671407"


@pytest.fixture
def base_data_for_filter_by_state_1():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def base_data_for_filter_by_state_2():
    return [
        {"id": 41428162, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719061, "state": "EXECUTED", "date": "2016-03-30T02:08:58.425572"},
        {"id": 594226850, "state": "CANCELED", "date": "2011-09-12T21:27:25.241689"},
        {"id": 615064000, "state": "EXECUTED", "date": "2013-11-14T08:21:33.419441"},
    ]


@pytest.fixture
def base_data_for_filter_by_state_3():
    return [
        {"id": 11128162, "state": "CANCELED", "date": "2003-07-03T18:35:29.512364"},
        {"id": 222719061, "state": "CANCELED", "date": "2001-09-30T02:08:58.425572"},
        {"id": 517226850, "state": "CANCELED", "date": "2017-06-12T21:27:25.241689"},
        {"id": 731064000, "state": "CANCELED", "date": "2013-12-14T08:21:33.419441"},
    ]


@pytest.fixture
def base_key_to_filter():
    return "CANCELED"
