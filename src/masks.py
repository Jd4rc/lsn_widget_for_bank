def get_mask_card_number(card_number: int) -> str:
    """ " Returns the mask card number"""
    str_card_number = str(card_number)
    return f"{str_card_number[:4]} {str_card_number[5:7]}** **** {str_card_number[-4:]}"


def get_mask_account(mask_account: int) -> str:
    """ " Returns the mask account"""
    str_mask_account = str(mask_account)
    return f"**{str_mask_account[-4:]}"
