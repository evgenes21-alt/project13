from datetime import datetime


datas = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(transactions: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция, которая принимает список словарей и опционально значение для ключа (по умолчанию 'EXECUTED')."""
    """Функция возвращает новый список словарей, содержащий только те словари,"""
    """у которых ключ state соответствует указанному значению."""

    return [
        transaction for transaction in transactions if transaction["state"] == state
    ]


print(filter_by_state(datas))
print(filter_by_state(datas, "CANCELED"))


def sort_by_date(transactions, reverse=True):
    """Функция,  которая принимает список словарей и необязательный параметр,"""
    """задающий порядок сортировки (по умолчанию — убывание)"""
    """Функция должна возвращать новый список, отсортированный по дате (date)."""

    return sorted(
        transactions, key=lambda x: datetime.fromisoformat(x["date"]), reverse=reverse
    )


print(datas)
