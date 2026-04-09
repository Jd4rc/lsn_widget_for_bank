def get_mask_card_number(card_number: int | str) -> str:
    """ " Returns the mask card number"""
    str_card_number = str(card_number)

    if not str_card_number.isdigit():
        raise TypeError("card number must contain only digits")

    if len(str_card_number) != 16:
        raise ValueError("length must be 16")

    return f"{str_card_number[:4]} {str_card_number[4:6]}** **** {str_card_number[-4:]}"


def get_mask_account(mask_account: int | str) -> str:
    """ " Returns the mask account"""
    str_mask_account = str(mask_account)

    if not str_mask_account.isdigit():
        raise TypeError("account number must contain only digits")

    if len(str_mask_account) != 20:
        raise ValueError("length must be 20")

    return f"**{str_mask_account[-4:]}"
