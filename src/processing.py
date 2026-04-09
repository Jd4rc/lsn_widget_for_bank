def filter_by_state(
    list_to_filter: list[dict[str, str | int]], key_to_filter: str = "EXECUTED"
) -> list[dict[str, str | int]]:
    """ "
    Принимает список словарей и опционально значение для ключа,
    возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению
    """
    result: list[dict[str, str | int]] = []

    for el in list_to_filter:
        if el["state"] == key_to_filter:
            result.append(el)

    return result


def sort_by_date(unsorted_data: list[dict[str, str | int]], reverse: bool = True) -> list[dict[str, str | int]]:
    """ "
    Принимает список словарей и параметр
    направления сортировки. Возвращает новый список, отсортированный
    по ключу 'date'
    """

    sorted_data = sorted(unsorted_data, key=lambda item: item["date"], reverse=reverse)

    return sorted_data
