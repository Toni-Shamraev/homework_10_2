from src.masks import get_mask_card_number, get_mask_account

def test_get_mask_card_maestro(maestro):
    assert get_mask_card_number("Maestro 1596837868705199") == maestro

def test_get_mask_card_mastercard(mastercard):
    assert get_mask_card_number("MasterCard 300734726758") == mastercard

def test_get_mask_card_empty_string(empty_string):
    assert get_mask_card_number("") == empty_string

def test_get_first_mask_account(first_account):
    assert get_mask_account("Счет 73654108430135874305") == first_account

def test_get_second_mask_account(second_account):
    assert get_mask_account("Счет 473678894779589") == second_account

def test_get_empty_mask_account(empty_account):
        assert get_mask_account("") == empty_account