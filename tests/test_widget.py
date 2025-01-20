import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize('value, expected', [
    ("Счет 73654108430135874305", 'Счет **4305'),
    ("Счет 3033474447895560", "Счет **5560"),
    ("", ""),
    ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353")
])
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected

def test_first_get_date(first_date):
    assert get_date("2024-03-11T02:26:18.671407") == first_date

def test_second_get_date(second_date):
    assert get_date("2023-12-02 T04322:26:18.643271407") == second_date

def test_get_date_empty(empty_date):
    assert get_date("") == empty_date