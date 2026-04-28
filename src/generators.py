from collections.abc import Iterator


def filter_by_currency(
    data: list[dict[str, int | str | dict[str, dict[str, str]]]], currency: str
) -> Iterator[dict[str, int | str | dict[str, str]]]:
    """
    фильтрует список операций по коду валюты (operationAmount.currency.code)

    возвращает генератор словарей операций с совпадающим значением currency
    """
    if not isinstance(data, list):
        raise TypeError("тип входных данных должен быть список")

    for x in data:
        if not isinstance(x, dict):
            raise TypeError("тип элементов входных данных должен быть словарь")
        if not isinstance(x.get("operationAmount"), dict):
            raise TypeError("тип \"operationAmount\" данных должен быть словарь")
        if not x["operationAmount"].get("currency"):
            raise KeyError("для фильтрации необходимо наличие ключа \"currency\"")
        if not isinstance((x["operationAmount"]).get("currency"), dict):
            raise TypeError("тип ключа \"currency\" должен быть словарем")
        if not x["operationAmount"]["currency"].get("code"):
            raise KeyError("для фильтрации необходимо наличие ключа \"code\"")
        if x["operationAmount"]["currency"]["code"] == currency:
            yield x


def transaction_descriptions(data: list[dict[str, int | str | dict[str, dict[str, str]]]]) -> Iterator[str]:
    """
    принимает список словарей с операциями

    возвращает итератор строк с описанием операций

    выбрасывает исключение KeyError, если в операции нет ключа "description"
    """
    for x in data:
        if "description" not in x:
            raise KeyError("описание операции отсутствует")
        yield x["description"]


def card_number_generator(range_from: int, range_to: int) -> Iterator[str]:
    """
    генерирует номера банковских карт в заданном числовом диапазоне

    возвращает итератор строк в формате "XXXX XXXX XXXX XXXX",
    где номер формируется из числа с ведущими нулями до 16 цифр

    выбрасывает исключение ValueError если range_from > range_to
    """
    if range_from > range_to:
        raise ValueError("первый аргумент должен быть меньше второго")

    number = range_from
    while int(number) <= range_to:
        num_str = f"{number:016d}"

        yield f"{num_str[:4]} {num_str[4:8]} {num_str[8:12]} {num_str[12:]}"
        number += 1
