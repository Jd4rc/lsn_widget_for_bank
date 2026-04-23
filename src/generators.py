from collections.abc import Iterator

def filter_by_currency(
        data: list[dict[str, int | str | dict[str, dict[str, str]]]],
        currency: str
) -> Iterator[dict[str, int | str | dict[str, str]]]:
    return (x for x in data if x["operationAmount"]["currency"]["code"] == currency)


def transaction_descriptions(
        data: list[dict[str, int | str | dict[str, dict[str, str]]]]
) -> Iterator[str]:
    return (x["description"] for x in data)