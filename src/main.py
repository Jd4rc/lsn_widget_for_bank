from .masks import get_mask_account
from .masks import get_mask_card_number

mask_account = get_mask_account(73654108430135874305)
mask_card_number = get_mask_card_number(7000792289606361)

print(mask_account)
print(mask_card_number)
