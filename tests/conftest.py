from typing import Any, Dict, List

import pytest


@pytest.fixture
def sample_data() -> List[Dict[str, Any]]:
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-15T10:30:00"},
        {"id": 2, "state": "PENDING", "date": "2023-01-10T12:15:00"},
        {"id": 3, "state": "EXECUTED", "date": "2023-01-20T08:45:00"},
        {"id": 4, "state": "CANCELED", "date": "2023-01-05T14:20:00"},
        {"id": 5, "state": "EXECUTED", "date": "2023-01-20T08:45:00"},
    ]


@pytest.fixture
def empty_transactions() -> List[Dict[str, Any]]:
    """Пустой список транзакций"""
    return []


@pytest.fixture
def card_numbers() -> List[str]:
    """Валидные номера карт для тестирования"""
    return [
        "7000792289606361",
        "1234567812345678",
        "0000000000000000",
        "9999999999999999",
    ]


@pytest.fixture
def invalid_card_numbers() -> List[str]:
    """Невалидные номера карт для тестирования"""
    return [
        "1234",  # Слишком короткий
        "12345678123456789",  # Слишком длинный
        "abcdefghijklmnop",  # Буквы
        "",  # Пустая строка
        "123456781234567a",  # Смешанные символы
    ]


@pytest.fixture
def account_numbers() -> List[int]:
    """Валидные номера счетов для тестирования"""
    return [
        73654108430135874305,
        12345678901234567890,
        1234,
        0,
        9999999999999999,
    ]


@pytest.fixture
def card_data() -> List[str]:
    """Данные карт для тестирования mask_account_card"""
    return [
        "Visa Platinum 7000792289606361",
        "Maestro 1234567812345678",
        "МИР 0000000000000000",
        "MasterCard 9999888877776666",
    ]


@pytest.fixture
def account_data() -> List[str]:
    """Данные счетов для тестирования mask_account_card"""
    return [
        "Счет 73654108430135874305",
        "Счет 12345678901234567890",
        "Счет 00000000000000000001",
    ]


@pytest.fixture
def date_strings() -> List[str]:
    """Различные форматы дат для тестирования"""
    return [
        "2023-12-31",
        "2020-02-29",
        "1999-01-01",
        "2000-12-31T23:59:59",
        "2023-06-15T00:00:00Z",
        "2023/12/31",
        "31-12-2023",
        "Dec 31 2023",
        "15 June 2023",
        "2023.06.15",
    ]


@pytest.fixture
def invalid_dates() -> List[str]:
    """Невалидные данные дат для тестирования"""
    return [
        "",
        "not a date",
        "123456",
        "2023-13-01",  # Несуществующий месяц
        "2023-02-30",  # Несуществующая дата
    ]


@pytest.fixture
def mixed_state_data() -> List[Dict[str, Any]]:
    """Данные с различными состояниями для расширенного тестирования"""
    return [
        {"id": 100, "state": "EXECUTED", "date": "2024-01-01T00:00:00"},
        {"id": 101, "state": "PENDING", "date": "2024-01-02T12:00:00"},
        {"id": 102, "state": "CANCELED", "date": "2024-01-03T23:59:59"},
        {"id": 103, "state": "FAILED", "date": "2024-01-04T06:30:00"},
        {"id": 104, "state": "EXECUTED", "date": "2024-01-05T18:45:00"},
    ]


@pytest.fixture
def list_of_transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.fixture
def list_of_transactions_for_regex():
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {
                "amount": "48223.05",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 214024827,
            "state": "EXECUTED",
            "date": "2018-12-20T16:43:26.929246",
            "operationAmount": {
                "amount": "70946.18",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "from": "Счет 10848359769870775355",
            "to": "Счет 21969751544412966366",
        },
        {
            "id": 522357576,
            "state": "EXECUTED",
            "date": "2019-07-12T20:41:47.882230",
            "operationAmount": {
                "amount": "51463.70",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "from": "Счет 48894435694657014368",
            "to": "Счет 38976430693692818358",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 596171168,
            "state": "EXECUTED",
            "date": "2018-07-11T02:26:18.671407",
            "operationAmount": {
                "amount": "79931.03",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Открытие вклада",
            "to": "Счет 72082042523231456215",
        },
    ]


@pytest.fixture
def list_of_transactions_curr_empty():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "", "code": ""},
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        }
    ]


@pytest.fixture
def list_of_transactions_no_curr():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "EUR", "code": "EUR"},
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        }
    ]


@pytest.fixture
def list_of_transactions_empty():
    return []


@pytest.fixture
def some_transaction_usd():
    return {
        "id": 939719840,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "1500.6",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }


@pytest.fixture
def some_transaction_rub():
    return {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
