def mask_account_card(account_card: str) -> str:
    """ " Returns the mask card number or account"""
    import re

    from src.masks import get_mask_account
    from src.masks import get_mask_card_number

    number_account_card = re.sub(r"[^\d+]", "", account_card)
    string_account_card = re.sub(r"[^\D\s$]", "", account_card)

    if len(number_account_card) == 16:
        number = get_mask_card_number(int(number_account_card))
    else:
        number = get_mask_account(int(number_account_card))

    message = f"{string_account_card}{number}"

    return message


def get_date(date: str) -> str | None:
    """ " Returns the formatted date"""
    import re

    pattern = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})T(\d{2}):(\d{2}):(\d{2}).(\d{6})"

    if not re.fullmatch(pattern, date):
        raise ValueError()

    formatted_date = re.sub(
        pattern,
        r"\g<day>.\g<month>.\g<year>",
        date,
    )
    return formatted_date
