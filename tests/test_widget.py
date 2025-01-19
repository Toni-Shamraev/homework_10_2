import pytest

from src.widget import mask_account_card


@pytest.mark.parametrize('value, expected', [
    ("Счет 73654108430135874305", 'Счет **4305'),
    ("Счет 35383033474447895560", "Счет **5560")
])
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected
