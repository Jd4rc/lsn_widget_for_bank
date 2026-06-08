import logging

logger = logging.getLogger(__name__)

def get_mask_card_number(card_number: int | str) -> str:
    """ " Returns the mask card number"""

    logger.info("Masking card number")

    str_card_number = str(card_number)

    logger.debug("Card number length: %s", len(str_card_number))

    if not str_card_number.isdigit():
        logger.error("Card number contains non-digit characters")
        raise TypeError("card number must contain only digits")

    if len(str_card_number) != 16:
        logger.error(
            "Invalid card number length: %s",
            len(str_card_number)
        )
        raise ValueError("length must be 16")


    masked_number = (
        f"{str_card_number[:4]}"
        f" {str_card_number[4:6]}**"
        f" **** {str_card_number[-4:]}"
    )

    logger.info("Card number masked successfully")

    return masked_number


def get_mask_account(mask_account: int | str) -> str:
    """ " Returns the mask account"""

    logger.info("Masking account number")

    str_mask_account = str(mask_account)

    logger.debug("Account number length: %s", len(str_mask_account))

    if not str_mask_account.isdigit():
        logger.error("Account number contains non-digit characters")
        raise TypeError("account number must contain only digits")

    if len(str_mask_account) != 20:
        logger.error(
            "Invalid account number length: %s",
            len(str_mask_account)
        )
        raise ValueError("length must be 20")

    masked_account = f"**{str_mask_account[-4:]}"

    logger.info("Account number masked successfully")

    return masked_account
