import pytest
from src.processing import filter_by_state, sort_by_date

def test_filter_by_state_with_base_data_1(base_data_for_filter_by_state_1):
    assert filter_by_state(base_data_for_filter_by_state_1) == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]

def test_filter_by_state_with_base_data_2(base_data_for_filter_by_state_2):
    assert filter_by_state(base_data_for_filter_by_state_2) == [
        {'id': 41428162, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719061, 'state': 'EXECUTED', 'date': '2016-03-30T02:08:58.425572'},
        {'id': 615064000, 'state': 'EXECUTED', 'date': '2013-11-14T08:21:33.419441'}
    ]

def test_filter_by_state_with_base_data_3(base_data_for_filter_by_state_3):
    assert filter_by_state(base_data_for_filter_by_state_3) == [

    ]

def test_filter_by_state_with_base_data_3_and_key_to_filter_par(base_data_for_filter_by_state_3, base_key_to_filter):
    assert filter_by_state(base_data_for_filter_by_state_3, base_key_to_filter) == [
        {'id': 11128162, 'state': 'CANCELED', 'date': '2003-07-03T18:35:29.512364'},
        {'id': 222719061, 'state': 'CANCELED', 'date': '2001-09-30T02:08:58.425572'},
        {'id': 517226850, 'state': 'CANCELED', 'date': '2017-06-12T21:27:25.241689'},
        {'id': 731064000, 'state': 'CANCELED', 'date': '2013-12-14T08:21:33.419441'}
    ]

@pytest.mark.parametrize('data, state, expected', [
    ([
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ],
        'NOT_EXIST',
        []
    ),
    ([
        {'id': 41428162, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719061, 'state': 'EXECUTED', 'date': '2016-03-30T02:08:58.425572'},
        {'id': 594226850, 'state': 'CANCELED', 'date': '2011-09-12T21:27:25.241689'},
        {'id': 615064000, 'state': 'EXECUTED', 'date': '2013-11-14T08:21:33.419441'}
    ],
        'EXECUTED',
    [
        {'id': 41428162, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719061, 'state': 'EXECUTED', 'date': '2016-03-30T02:08:58.425572'},
        {'id': 615064000, 'state': 'EXECUTED', 'date': '2013-11-14T08:21:33.419441'}
    ]),
    ([
        {'id': 11128162, 'state': 'CANCELED', 'date': '2003-07-03T18:35:29.512364'},
        {'id': 222719061, 'state': 'CANCELED', 'date': '2001-09-30T02:08:58.425572'},
        {'id': 517226850, 'state': 'CANCELED', 'date': '2017-06-12T21:27:25.241689'},
        {'id': 731064000, 'state': 'CANCELED', 'date': '2013-12-14T08:21:33.419441'}
    ],
        'CANCELED',
    [
        {'id': 11128162, 'state': 'CANCELED', 'date': '2003-07-03T18:35:29.512364'},
        {'id': 222719061, 'state': 'CANCELED', 'date': '2001-09-30T02:08:58.425572'},
        {'id': 517226850, 'state': 'CANCELED', 'date': '2017-06-12T21:27:25.241689'},
        {'id': 731064000, 'state': 'CANCELED', 'date': '2013-12-14T08:21:33.419441'}
    ])
])
def test_filter_by_state_with_parametrized(data, state, expected):
    assert filter_by_state(data, state) == expected


@pytest.mark.parametrize('data, reverse, expected', [
    (
        [
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
        ],
        True,
        [
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}

        ]
    ),
    (
        [
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
        ],
        False,
        [
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
        ]
    )
])
def test_sort_by_date_with_parametrized(data, reverse, expected):
    assert sort_by_date(data, reverse) == expected

def test_sort_by_state_with_diff_time_format():
    assert sort_by_date(
        [
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03'}
        ]
    ) == [
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018'}
        ]

def test_sort_by_state_with_empty_list():
    assert sort_by_date([]) == []

def test_sort_by_state_with_another_type_data():
    assert sort_by_date({}) == []