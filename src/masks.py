import textwrap


def get_mask_card_number(card_numbers: str) -> str:
    """Маскируем номер карты и возвращаем разбитый номер"""
    hide_numbers = card_numbers[-10:] + "******" + card_numbers[-4:]
    new_numbers = " ".join(textwrap.wrap(hide_numbers, 4))[-20:]
    result = card_numbers[:-17] + new_numbers
    return result


def get_mask_account(account_numbers: str) -> str:
    """Маскируем номер счёта и возвращаем последние 6 символов"""
    digits = str(account_numbers)[-6:]
    hide_numbers = "**" + digits[-4:]
    result = account_numbers[:5] + hide_numbers
    return result
