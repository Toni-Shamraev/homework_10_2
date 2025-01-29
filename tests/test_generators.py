import pytest

from src.generators import (card_number_generator, filter_by_currency,
                            transactions, transaction_descriptions)


def test_filter_by_usd():
    currency_code = filter_by_currency(transactions, "USD")
    assert next(currency_code) == transactions[0]
    assert next(currency_code) == transactions[1]
    assert next(currency_code) == transactions[3]

def test_filter_by_rub():
    currency_code = filter_by_currency(transactions, "RUB")
    assert next(currency_code) == transactions[2]
    assert next(currency_code) == transactions[4]


def test_transaction_descriptions():
    disc_info = transaction_descriptions(transactions)
    assert next(disc_info) == "Перевод организации"
    assert next(disc_info) == "Перевод со счета на счет"
    assert next(disc_info) == "Перевод со счета на счет"
    assert next(disc_info) == "Перевод с карты на карту"
    assert next(disc_info) == "Перевод организации"


def test_card_number_generator():
    generator = card_number_generator(1, 5)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"
    assert next(generator) == "0000 0000 0000 0004"
    assert next(generator) == "0000 0000 0000 0005"
    with pytest.raises(StopIteration):
        next(generator)