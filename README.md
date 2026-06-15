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

## Возможности проекта

- Маскирование карт и счетов
- Фильтрация операций
- Сортировка по дате
- Генераторы транзакций
- Работа с JSON
- Конвертация валют через API
- Логирование
- Загрузка транзакций из JSON, CSV и XLSX
- Интерактивная работа через консольное меню
- Фильтрация по статусу операции
- Фильтрация только рублевых операций
- Поиск операций по описанию
- Подсчет операций по категориям
- Сортировка операций по дате
- Форматированный вывод операций

## Использование

### Отфильтровать список операций по коду валюты
1. В файле `src/main.py` имортировать функцию `filter_by_currency`
2. В файле `src/main.py` написать вызов функции `filter_by_currency`, передать аргумент типа `dict[list]`, написать в файле `main.py` команду `print` для вызываемой функции, чтобы увидеть возращаемого значение функции в консоле
3. Выполнить в косноле команду `py.exe -m src.main`

### получить описание транзакции по одной
1. В файле `src/main.py` имортировать функцию `transaction_descriptions`
2. В файле `src/main.py` написать вызов функции `transaction_descriptions`, передать аргумент типа `dict[list]`, написать в файле `main.py` команду `print(next())` для вызываемой функции, чтобы увидеть возращаемое значение функции в консоле
3. Выполнить в косноле команду `py.exe -m src.main`

### Сгенерировать номера банковских карт в заданном числовом диапазоне по одному в формате `XXXX XXXX XXXX XXXX`
1. В файле `src/main.py` имортировать функцию `card_number_generator`
2. В файле `src/main.py` написать вызов функции `card_number_generator`, передать два аргумента, описывающих дипазон, в котором будут генерироваться номера карт, написать в файле `main.py` команду `print(next())` для вызываемой функции, чтобы увидеть возращаемые значения функции в консоле
3. Выполнить в косноле команду `py.exe -m src.main`

### Логирование вызова функций
* декоратор log из модуля decorators.py, который позволяет логировать:

- начало выполнения функции,
- результат выполнения функции
- ошибки и исключения
- завершение выполнения функции.

* Декоратор поддерживает:

- вывод логов в консоль,
- запись логов в текстовый .txt файл,
- автоматическое создание директории data/.

### Работа с транзакциями

#### Загрузка транзакций из JSON

Функция `load_transactions()` загружает данные из JSON-файла и возвращает список транзакций.

#### Конвертация суммы транзакции

Функция `get_transaction_amount()`:

- поддерживает RUB, USD и EUR;
- автоматически конвертирует USD и EUR в RUB;
- использует внешний API обменных курсов;
- возвращает сумму в рублях.

## Работа с транзакциями

## Загрузка транзакций

Проект поддерживает загрузку транзакций из файлов следующих форматов:

* `.json`
* `.csv`
* `.xlsx`

Основная функция:

```
load_transactions(filepath: str) -> list[dict[str, Any]]
```

Функция определяет формат файла по расширению и вызывает нужный загрузчик:

* JSON читается через модуль `json`
* CSV читается через встроенный модуль `csv`
* XLSX читается через библиотеку `pandas`

Пример использования:

```
transactions = load_transactions("data/operations.json")
transactions = load_transactions("data/transactions.csv")
transactions = load_transactions("data/transactions_excel.xlsx")
```

Если файл не найден, содержит некорректные данные или формат не поддерживается, функция возвращает пустой список.

## Зависимости

Для работы с Excel-файлами используется `pandas` и `openpyxl`.

### Конвертация суммы транзакции

Функция `get_transaction_amount()`:

- поддерживает RUB, USD и EUR;
- автоматически конвертирует USD и EUR в RUB;
- использует внешний API обменных курсов;
- возвращает сумму в рублях.

## Логирование

Проект использует модуль `logging`

Логи записываются в директорию:

logs/

Формат записи:

2026-06-08 14:25:10,123 - src.utils - INFO - Processing transaction amount

## Консольное приложение

Проект содержит консольное приложение для анализа банковских транзакций.

Для запуска:

```bash
py.exe -m src.main
```

После запуска пользователь может:

1. Выбрать источник данных:
   - JSON
   - CSV
   - XLSX

2. Отфильтровать операции по статусу:
   - EXECUTED
   - CANCELED
   - PENDING

3. Выполнить дополнительные фильтрации:
   - только рублевые операции;
   - поиск по слову в описании;
   - сортировка по дате.

После обработки программа выводит итоговый список операций в удобном формате.


## Поиск операций

Функция:

```
process_bank_search(data: list[dict], search: str) -> list[dict]
```

Выполняет поиск операций по полю `description`.

Поиск выполняется с использованием регулярных выражений (`re`) без учета регистра.

Пример:

```
process_bank_search(transactions, "перевод")
```

## Поиск операций

Функция:

```
process_bank_search(data: list[dict], search: str) -> list[dict]
```

Выполняет поиск операций по полю `description`.

Поиск выполняется с использованием регулярных выражений (`re`) без учета регистра.

Пример:

```
process_bank_search(transactions, "перевод")
```

## Подсчет операций по категориям

Функция:

```
process_bank_operations(data: list[dict], categories: list[str]) -> dict
```

Подсчитывает количество операций для каждой указанной категории на основе поля `description`.

Для подсчета используется `Counter` из модуля `collections`.

Пример результата:

```
{
    "Перевод": 15,
    "Открытие вклада": 4,
    "Оплата услуг": 2
}
```

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
        "description": "Перевод организации",
        "operationAmount": {
            "currency": {"code": "USD"}
        }
    },
    {
        "description": "Перевод со счета на счет",
        "operationAmount": {
            "currency": {"code": "RUB"}
        }
    },
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
    {"description": "Перевод организации"},
    {"description": "Перевод со счета на счет"},
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


* Логирование в консоль
```
File: src/main.py

from src.decorators import log


@log()
def add(a, b):
    return a + b


result = add(2, 3)

print(result)

Команда в консоли: py.exe -m src.main

>>> [LOG][2026-05-20 12:00:00] Начало выполнения функции: add
[LOG][2026-05-20 12:00:00] Результат функции: 5
[LOG][2026-05-20 12:00:00] Конец выполнения функции: add
```

* Логирование в файл
```
File: src/main.py

from src.decorators import log


@log(filename="logs.txt")
def divide(a, b):
    return a / b


divide(10, 2)
```
- После выполнения автоматически создается структура:
`.project/data/logs.txt`

* Логирование ошибок
``` 
File: src/main.py

from src.decorators import log


@log()
def divide(a, b):
    return a / b


divide(10, 0)

Команда в консоли: py.exe -m src.main

>>> [ERROR][2026-05-20 12:00:00]
В функции divide возникла ошибка: division by zero.
Входные параметры: (10, 0), {}
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
- декоратор `log` (логирование в консоль или файл с раширением txt)
### Обрати внимание
- Дата в функции `get_date` на входе должна быть в формате `YYYY-MM-DDTHH:MM:SS` 
- Проект использует Poetry для работы с зависимостями

### Используемые технологии

- Python 3.14+
- Poetry
- requests
- python-dotenv
- pytest
- pytest-cov
- black
- flake8
- mypy
- isort