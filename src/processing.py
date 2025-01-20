from typing import Dict, List

bank_operations = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(bank_info: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Функция обрабатывающая список словарей с данными о банковских операциях"""
    new_list = []
    for name in bank_info:
        if name.get("state") in state:
            new_list.append(name)
        elif name.get("state") not in state:
            new_list.append(name)
    return new_list


def sort_by_date(bank_info: List[Dict], direction: bool=False) -> List[Dict]:
    """"Функция сортировки списка по дате из словарей"""
    return sorted(bank_info, key=lambda x: x["date"], reverse=direction)
