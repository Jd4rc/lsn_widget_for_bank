def mask_account_card(par:str) -> str:
    """" Returns the mask card number or account"""
    import re
    from masks import get_mask_account
    from masks import get_mask_card_number

    foo = re.sub(r'[^\d+]', '', par)
    bar = re.sub(r'[^\D\s$]', '', par)

    if len(foo) == 16:
        number = get_mask_card_number(int(foo))
    else:
        number = get_mask_account(int(foo))

    mask = f'{bar}{number}'

    return mask
