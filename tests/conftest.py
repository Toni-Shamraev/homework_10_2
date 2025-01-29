import pytest

from src.generators import card_number_generator


@pytest.fixture
def maestro():
    return "Maestro 1596 83** **** 5199"


@pytest.fixture
def mastercard():
    return "MasterCard 7158 30** **** 6758"


@pytest.fixture
def empty_string():
    return ""


@pytest.fixture
def first_account():
    return "Счет **4305"


@pytest.fixture
def second_account():
    return "Счет **9589"


@pytest.fixture
def empty_account():
    return ""


@pytest.fixture
def first_date():
    return "11.03.2024"


@pytest.fixture
def second_date():
    return "02.12.2023"


@pytest.fixture
def empty_date():
    return ""


