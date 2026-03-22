def filter_by_state(par1: list, par2: str = "EXECUTED") -> list:
    """ "
    Принимает список словарей и опционально значение для ключа,
    возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению
    """
    result = []

    for el in par1:
        if el["state"] == par2:
            result.append(el)

    return result


def sort_by_date(par1=list, par2: bool = True) -> list:
    """ "
    Принимает список словарей и необязательный параметр,
    задающий порядок сортировки. Возвращает отсортированный список
    словарей по дате
    """

    sorted_data = sorted(par1, key=lambda k: k["date"], reverse=par2)

    return sorted_data
