from collections.abc import Iterator

def filter_by_currency(
        data: list[dict[str, int | str | dict[str, dict[str, str]]]],
        currency: str
) -> Iterator[dict[str, int | str | dict[str, str]]]:
    yield from (x for x in data if x["operationAmount"]["currency"]["code"] == currency)


