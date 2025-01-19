import masks


def mask_account_card(account_info: str) -> str:
    """Функция обработки и карт и счёта"""
    if account_info[:4] == "Счет":
        return str(masks.get_mask_account(account_info))
    else:
        return str(masks.get_mask_card_number(account_info))


def get_date(date: str) -> str:
    """Функция конвертирования даты"""
    result = date[8:10] + "." + date[5:7] + "." + date[:4]
    return result


print(mask_account_card('Счет 35383033474447895560'))
print(get_date('2024-03-11T02:26:18.671407'))
