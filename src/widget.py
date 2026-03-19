def mask_account_card(par: str) -> str:
    """ " Returns the mask card number or account"""
    import re

    from src.masks import get_mask_account
    from src.masks import get_mask_card_number

    foo = re.sub(r"[^\d+]", "", par)
    bar = re.sub(r"[^\D\s$]", "", par)

    if len(foo) == 16:
        number = get_mask_card_number(int(foo))
    else:
        number = get_mask_account(int(foo))

    mask = f"{bar}{number}"

    return mask


def get_date(par: str) -> str:
    """ " Returns the format date"""
    import re

    par = re.sub(
        r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})T(\d{2}):(\d{2}):(\d{2}).(\d{6})",
        r"\g<day>.\g<month>.\g<year>",
        par,
    )
    return par
