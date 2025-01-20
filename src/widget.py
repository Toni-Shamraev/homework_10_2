from src import masks


def mask_account_card(account_info: str) -> str:
    """Функция обработки и карт и счёта"""
    if account_info[:4] == "Счет":
        return str(masks.get_mask_account(account_info))
    else:
        return str(masks.get_mask_card_number(account_info))


def get_date(date: str) -> str:
    """Функция конвертирования даты"""
    if date != "":
        result = date[8:10] + "." + date[5:7] + "." + date[:4]
        return result
    elif date == "":
        return ""
