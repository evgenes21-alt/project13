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
