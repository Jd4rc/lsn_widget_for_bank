# Учебный проект для банковского приложения

## Репозиторий образовательного проекта на Python, посвященного созданию функций для простого банковского приложения, охватывающего основные концепции и практические навыки разработки.

## Установка

1. Клонируйте репозиторий:

Если https
```
git clone https://github.com/Jd4rc/lsn_widget_for_bank.git
```
Если ssh
```
git clone git@github.com:Jd4rc/lsn_widget_for_bank.git
```

## Использование

### Создание маски для твоего карточки

1. В файле `src/main.py` имортировать функию `mask_account_card` из модуля `widget.py`
2. В файле `src/main.py` написать вызов функции `mask_account_card()`, передать аргумент типа `str` в формате `Master Card 'число из 16 цифр'`, написать в файле `main.py` команду `print` для вызываемой функции, чтобы увидеть возращаемого значение функции в консоле
3. Выполнить в косноле команду `py.exe -m src.main`

### Создание маски для твоей счета

1. В файле `src/main.py` имортировать функию `mask_account_card` из модуля `widget.py`
2. Написать вызов функции `mask_account_card()`, передать аргумент типа `str` в формате `Счет 'число из 20 цифр'`, написать в файле `main.py` команду `print` для вызываемой функции, чтобы увидеть возращаемого значение функции в консоле
3. Выполнить в косноле команду `py.exe -m src.main`

###  Отфильтровать список словарей по ключу state

1. В файле `src/main.py` имортировать функию `filter_by_state` из модуля `processing.py`
2. Написать вызов функции `filter_by_state`, передать обязательный аргумент типа `list`, содержащий в себе словари, в каждом из которых может быть ключ `state`, - его значение ипользуется для 2-ого параметра, в формате `list[dict{}]`. Второй аргумент является необязательным и содержит в себе значение по-умолчанию `EXECUTED`. Написать в файле `main.py` команду `print` для вызываемой функции, чтобы увидеть возращаемого значение функции в консоле
3. Выполнить в косноле команду `py.exe -m src.main`

###  Отфильтровать список словарей по ключу date и возможностью задать порядок сортировки

1. В файле `src/main.py` имортировать функию `sort_by_date` из модуля `processing.py`
2. Написать вызов функции `sort_by_date`, передать обязательный аргумент типа `list`, содержащий в себе словари, в каждом из которых есть ключ `date`, - по нему производится сортировка, в формате `list[dict{}]`. Второй аргумент является необязательным и содержит в себе `bool` тип данных со значением по-умолчанию `True`, что определяет порядок сортировки
3. Выполнить в косноле команду `py.exe -m src.main`

###  Получить дату в нужном формате

1. В файле `src/main.py` имортировать функию `get_date`
2. В файле `src/main.py` написать вызов функции `get_date`, передать аргумент типа `str` в формате `2024-03-11T02:26:18.671407`, написать в файле `main.py` команду `print` для вызываемой функции, чтобы увидеть возращаемого значение функции в консоле
3. Выполнить в косноле команду `py.exe -m src.main`

## Примеры использования

* Создание маски для твоего карточки

```
File: src/main.py

from src.widget import mask_account_card

result = mask_account_card("Visa Platinum 7000792289606361")

print(result)

Команда в консоли: py.exe -m src.main

>>> Visa Platinum 7000 92** **** 6361
```

* Создание маски для твоей счета

```
File: src/main.py

from src.widget import mask_account_card

result = mask_account_card("Счет 73654108430135874305")

print(result)

Команда в консоли: py.exe -m src.main

>>> Счет **4305
```

* Отфильтровать список словарей по ключу state

```
File: src/main.py

from src.processing import filter_by_state

data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]

result = filter_by_state(data)

print(result)

Команда в консоли: py.exe -m src.main

>>> [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]
```
```
File: src/main.py

from src.processing import filter_by_state

data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]

result = filter_by_state(data, 'CANCELED')

print(result)

Команда в консоли: py.exe -m src.main

>>> [
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]

```

* Отфильтровать список словарей по ключу date и возможностью задать порядок сортировки

```
File: src/main.py

from src.processing import sort_by_date

data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]
    
result = sort_by_date(data)

print(result)

Команда в консоли: py.exe -m src.main

>>> [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]
```
```
File: src/main.py

from src.processing import sort_by_date

data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]
    
result = sort_by_date(data, False)

print(result)

Команда в консоли: py.exe -m src.main

>>> [
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
    ]
```

* Получить дату в нужном формате

```
File: src/main.py

from src.widget import get_date

data_to_format = "2024-03-11T02:26:18.671407"

result = get_date(data_to_format)

print(result)

Команда в консоли: py.exe -m src.main

>>> 11.03.2024
```

* отфильтровать список операций по коду валюты
```
File: src/main.py

from src.generators import filter_by_currency

transactions = (
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
)

result = filter_by_currency(transactions, "USD")

print(*result)

Команда в консоли: py.exe -m src.main

>>> {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        }
```

* получить описание транзакции по одной
```
File: src/main.py

from src.generators import transaction_descriptions

transactions = (
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
)

result = transaction_descriptions(transactions)

print(next(result))

Команда в консоли: py.exe -m src.main

>>> Перевод организации
    
```

* cгенерировать номера банковских карт в заданном числовом диапазоне по одному в формате `XXXX XXXX XXXX XXXX`
```
File: src/main.py

from src.generators import card_number_generator

result = card_number_generator(1, 5)

print(next(result))

Команда в консоли: py.exe -m src.main

>>> 0000 0000 0000 0001
```

## Тесты

### Установка 

* Установите poetry:
```
poetry install
```
* Активируйте виртуальное окружение
```
poetry env activate
```

### Запуск тестов

```
pytest 
```

### Структура
- Тесты расположены в директории tests/

### Что тестируется
- `mask_card_number` (возращает маску номера карты)
- `get_mask_account` (возращает маску счета клиента)
- `filter_by_state` (сортировка списка словарей по ключу state)
- `sort_by_date` (сортировка словарей по дате)
- `mask_account_card` (возращает маску карты или счета)
- `get_date` (форматирует дату в нужный формат)
- `filter_by_currency` (фильтрует список операций по коду валюты)
- `transaction_descriptions`(принимает список словарей с операциями, возвращает итератор строк с описанием операций)
- `card_number_generator` (генерирует номера банковских карт в заданном числовом диапазоне)

### Обрати внимание
- Дата в функции `get_date` на входе должна быть в формате `YYYY-MM-DDTHH:MM:SS` 
- Проект использует Poetry для работы с зависимостями

### Требования 
- Python 3.14+
- Poetry