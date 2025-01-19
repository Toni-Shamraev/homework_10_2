from src.masks import get_mask_card_number

def test_get_mask_card_number(maestro):
    assert get_mask_card_number("Maestro 1596837868705199") == maestro