from pathlib import Path
from src.utils import _load_json, _load_csv, _load_xlsx
from src.generators import filter_by_currency
from src.processing import process_bank_search, sort_by_date
from pprint import pprint



def main():
    print('Привет! Добро пожаловать в программу работы с банковскими транзакциями.')
    print('Выберите необходимый пункт меню:')
    print('1. Получить информацию о транзакциях из JSON-файла')
    print('2. Получить информацию о транзакциях из CSV-файла')
    print('3. Получить информацию о транзакциях из XLSX-файла')
    file_choice = input('Пользователь: ')
    if file_choice == '1':
        print('Для обработки выбран JSON-файл.')
        data = _load_json(Path('../data/operations.json'))
    elif file_choice == '2':
        print('Для обработки выбран CSV-файл.')
        data = _load_csv(Path('../data/transactions.csv'))
    elif file_choice == '3':
        print('Для обработки выбран XLSX-файл.')
        data = _load_xlsx(Path('../data/transactions_excel.xlsx'))
    else:
        print('Некорректный выбор. Завершение работы.')
        return
    # Допустим, data уже загружен
    print("После загрузки:", len(data))

    data = [
        item
        for item in data
        if isinstance(
            item.get(
                'operationAmount'
            ),
            dict)
        or item.get('amount')
    ]
    print("После проверки суммы:", len(data))

    statuses = ['EXECUTED', 'CANCELED', 'PENDING']
    while True:
        status = input('Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\nПользователь: ')
        status_upper = status.strip().upper()

        if status_upper in statuses:
            data = [
                    op
                    for op in data
                    if str(op.get(
                    'state', ''
                )).strip().upper() == status_upper
            ]
            print(f'Операции отфильтрованы по статусу "{status_upper}"')
            break
        else:
            print(f'Статус операции "{status}" недоступен.')
        # фильтр по статусу
        print("После статуса:", len(data))
    # Далее реализуйте сортировку, фильтрацию по валюте, поиску по описанию и вывод результата

    if input("Оставить только рублёвые операции? (да/нет): ").lower() == 'да':
        data = list(filter_by_currency(data, 'RUB'))

    # фильтр по валюте
    print("После валюты:", len(data))

     # Фильтрация по описанию
    if input("Фильтровать по слову в описании? (да/нет): ").lower() == 'да':
        word = input("Введите слово для фильтрации: ")
        data = process_bank_search(data, word)

    # 4. Сортировка по дате
    if input("Отсортировать операции по дате? (да/нет): ").lower() == 'да':
        order = input("Порядок сортировки: возрастание/убывание? ")
        data = sort_by_date(data, reverse=(order == 'убывание'))

    if data:
        pprint(data)  # красивая печать
    else:
        print("Нет операций, соответствующих условиям.")

if __name__ == '__main__':
    main()