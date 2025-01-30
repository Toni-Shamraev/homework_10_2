import pytest

from src.generators import (card_number_generator, filter_by_currency,
                            transaction_descriptions, transactions,)


def test_filter_by_usd():
    currency_code = filter_by_currency(transactions, "USD")
    assert next(currency_code) == transactions[0]
    assert next(currency_code) == transactions[1]
    assert next(currency_code) == transactions[3]


def test_filter_by_rub():
    currency_code = filter_by_currency(transactions, "RUB")
    assert next(currency_code) == transactions[2]
    assert next(currency_code) == transactions[4]


@pytest.mark.parametrize("y, expected", [("USD", [{
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        }, {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }, {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        }]),
                                         ("RUB", [{
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        }, {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }]),
                                         ("EUR", [])])
def test_filter_by_cur(y, expected):
    filtered_transactions = list(filter_by_currency(transactions, y))
    assert filtered_transactions == expected


def test_filter_by_cur_1(filter_cur_usd):
    generator = filter_by_currency(transactions, "USD")
    result = list(generator)
    assert result == filter_cur_usd


def test_filter_cur_2(filter_cur_rub):
    generator = filter_by_currency(transactions, "RUB")
    result = list(generator)
    assert result == filter_cur_rub


def test_filter_cur_3(filter_cur_eur):
    generator = filter_by_currency(transactions, "EUR")
    result = list(generator)
    assert result == filter_cur_eur


def test_transaction_descriptions():
    disc_info = transaction_descriptions(transactions)
    assert next(disc_info) == "Перевод организации"
    assert next(disc_info) == "Перевод со счета на счет"
    assert next(disc_info) == "Перевод со счета на счет"
    assert next(disc_info) == "Перевод с карты на карту"
    assert next(disc_info) == "Перевод организации"


@pytest.mark.parametrize("trans, expected", [(transactions,
                                              ["Перевод организации",
                                               "Перевод со счета на счет",
                                               "Перевод со счета на счет",
                                               "Перевод с карты на карту",
                                               "Перевод организации"])])
def test_transaction_desc(trans, expected):
    generator = transaction_descriptions(transactions)
    result = list(generator)
    assert result == expected


def test_transaction_desc_1(transaction_info_1):
    generator = transaction_descriptions(transactions)
    result = list(generator)
    assert result == transaction_info_1


def test_card_number_generator():
    generator = card_number_generator(1, 5)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"
    assert next(generator) == "0000 0000 0000 0004"
    assert next(generator) == "0000 0000 0000 0005"
    with pytest.raises(StopIteration):
        next(generator)


@pytest.mark.parametrize("start, end, expected",
                         [(1, 5, ["0000 0000 0000 0001",
                                 "0000 0000 0000 0002",
                                 "0000 0000 0000 0003",
                                 "0000 0000 0000 0004",
                                 "0000 0000 0000 0005"]),
                          (5, 9, ["0000 0000 0000 0005",
                                  "0000 0000 0000 0006",
                                  "0000 0000 0000 0007",
                                  "0000 0000 0000 0008",
                                  "0000 0000 0000 0009"]),
                          (0, 0, ["0000 0000 0000 0000"]),])
def test_card_number_gen(start, end, expected):
    generator = card_number_generator(start, end)
    result = list(generator)
    assert result == expected


def test_card_number_generation(card_numbers_1_5):
    expected_numbers = ["0000 0000 0000 0001",
                        "0000 0000 0000 0002",
                        "0000 0000 0000 0003",
                        "0000 0000 0000 0004",
                        "0000 0000 0000 0005"]
    assert card_numbers_1_5 == expected_numbers


def test_card_number_gen_zero(card_numbers_0_0):
    expected_numbers = ["0000 0000 0000 0000"]
    assert card_numbers_0_0 == expected_numbers
