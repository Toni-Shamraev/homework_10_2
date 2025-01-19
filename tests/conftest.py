import pytest


@pytest.fixture
def maestro():
    return "Maestro 1596 83** **** 5199"

@pytest.fixture
def mastercard():
    return "MasterCard 7158 30** **** 6758"

@pytest.fixture
def empty_string():
    return ""