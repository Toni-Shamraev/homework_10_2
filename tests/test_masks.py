from src.masks import get_mask_card_number

def test_get_mask_card_number(maestro):
    assert get_mask_card_number("Maestro 1596837868705199") == maestro


def test_get_mask_card_number(mastercard):
    assert get_mask_card_number("MasterCard 7158300734726758") == mastercard

def test_get_mask_card_number(empty_string):
    assert get_mask_card_number("") == empty_string