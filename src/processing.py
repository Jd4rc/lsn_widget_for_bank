import re


def filter_by_state(
    list_to_filter: list[dict[str, str | int]], key_to_filter: str = "EXECUTED"
) -> list[dict[str, str | int]]:
    """ "
    Принимает список словарей и опционально значение для ключа,
    возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению
    """
    result: list[dict[str, str | int]] = []

    key_to_filter = key_to_filter.upper()  # приводим к верхнему регистру

    for el in list_to_filter:
        state = str(el.get("state", "")).upper()
        if state == key_to_filter:
            result.append(el)

    return result


def sort_by_date(unsorted_data: list[dict[str, str | int]], reverse: bool = True) -> list[dict[str, str | int]]:
    """ "
    Принимает список словарей и параметр
    направления сортировки. Возвращает новый список, отсортированный
    по ключу 'date'
    """

    sorted_data = sorted(unsorted_data, key=lambda item: item.get("date", ""), reverse=reverse)

    return sorted_data


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    pattern = re.compile(re.escape(search), re.IGNORECASE)
    return [item for item in data if pattern.search(item.get("description", ""))]


def process_bank_operations(data: list[dict], categories: list[str]) -> dict:
    result = {category: 0 for category in categories}

    for item in data:
        description = item.get("description", "").lower()
        for category in categories:
            if category.lower() in description:
                result[category] += 1

    return result
