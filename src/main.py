# from src import logger_cfg
# import requests
# from src.masks import get_mask_card_number
# from src.utils import get_transaction_amount, load_transactions
#
# get_mask_card_number("1234567812345678")
#
# transactions = load_transactions(
#     "data/operations.json"
# )
#
# amounts = []
#
# for transaction in transactions:
#     if "operationAmount" not in transaction:
#         continue
#
#     currency = transaction["operationAmount"]["currency"]["code"]
#
#     if currency != "RUB":
#         continue
#
#     amount = get_transaction_amount(transaction)
#     amounts.append(amount)
#
# print(amounts)
#
# for transaction in transactions:
#     if "operationAmount" not in transaction:
#         continue
#
#     currency = transaction["operationAmount"]["currency"]["code"]
#
#     if currency in ("USD", "EUR"):
#         amount = get_transaction_amount(transaction)
#         print(amount)
#         break