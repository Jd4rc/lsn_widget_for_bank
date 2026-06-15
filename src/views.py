from src.masks import get_mask_account
from src.masks import get_mask_card_number
from src.widget import get_date


def format_operation(operation: dict) -> str:
    date = operation.get("date", "")
    date = get_date(date)
    description = operation.get("description", "")

    from_account = format_account(operation.get("from", ""))
    to_account = format_account(operation.get("to", ""))

    operation_amount = operation.get("operationAmount")

    if isinstance(operation_amount, dict):
        amount = operation_amount.get("amount")
        currency = operation_amount.get("currency", {}).get("code")
    else:
        amount = operation.get("amount")
        currency = operation.get("currency_code")

    return f"{date} {description}\n" f"{from_account} -> {to_account}\n" f"Сумма: {amount} {currency}"


def format_account(account: str) -> str:
    if not account:
        return ""

    if account.startswith("Счет"):
        number = account.split()[-1]
        return f"Счет {get_mask_account(number)}"

    parts = account.split()

    card_number = parts[-1]
    card_name = " ".join(parts[:-1])

    return f"{card_name} {get_mask_card_number(card_number)}"


def print_operations(data: list[dict]) -> None:
    print(f"Всего банковских операций в выборке: {len(data)}\n")

    for operation in data:
        print(format_operation(operation))
        print()
