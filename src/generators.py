from collections.abc import Iterator

def filter_by_currency(
        data: list[dict[str, int | str | dict[str, dict[str, str]]]],
        currency: str
) -> Iterator[dict[str, int | str | dict[str, str]]]:

    for x in data:
        if not isinstance(data, list):
            raise TypeError("тип входных данных должен быть список")
        if not isinstance(x, dict):
            raise TypeError("тип элементов входных данных должен быть словарь")
        if "currency" not in x["operationAmount"]:
            raise KeyError('для фильтрации необходимо наличие ключа \"currency\"')
        if x["operationAmount"]["currency"]["code"] == currency:
            yield x


def transaction_descriptions(
        data: list[dict[str, int | str | dict[str, dict[str, str]]]]
) -> Iterator[str]:
    for x in data:
        if "description" not in x:
            raise KeyError("описание операции отсутствует")
        yield x["description"]

def card_number_generator(
        range_from: int,
        range_to: int
) -> Iterator[str]:
    if range_from > range_to:
        raise ValueError('первый аргумент должен быть меньше второго')

    number = range_from
    while int(number) <= range_to:
        num_str = f"{number:016d}"

        yield f"{num_str[:4]} {num_str[4:8]} {num_str[8:12]} {num_str[12:]}"
        number += 1
