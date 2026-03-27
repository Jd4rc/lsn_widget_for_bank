def filter_by_state(list_to_filter: list, key_to_filter: str = "EXECUTED") -> list:
    """ "
    Принимает список словарей и опционально значение для ключа,
    возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению
    """
    result = []

    for el in list_to_filter:
        if el["state"] == key_to_filter:
            result.append(el)

    return result


def sort_by_date(unsorted_data: list, reverse: bool = True) -> list:
    """ "
    Принимает список словарей и параметр
    направления сортировки. Возвращает новый список, отсортированный
    по ключу 'date'
    """

    sorted_data = sorted(unsorted_data, key=lambda item: item["date"], reverse=reverse)

    return sorted_data
