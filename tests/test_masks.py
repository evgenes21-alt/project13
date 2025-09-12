import pytest


from src.masks import get_mask_card_number,get_mask_account

# Позитивные тесты - проверка корректного маскирования
@pytest.mark.parametrize(
    "card_number, expected_mask",
    [
        ("7000792289606361", "7000 79** **** 6361"),  # Стандартный номер
        ("0000000000000000", "0000 00** **** 0000"),  # Номер из нулей
        ("1234567812345678", "1234 56** **** 5678"),  # Другой номер
    ],
)
def test_card_masking_correct(card_number: str, expected_mask: str) -> None:
    """Проверяем корректное маскирование валидных номеров карт"""
    assert get_mask_card_number(card_number) == expected_mask


# Негативные тесты - проверка обработки ошибок
@pytest.mark.parametrize(
    "invalid_input, expected_error",
    [
        (None, "Номер карты не может быть None"),  # явно проверяем None
        ("", "Номер карты должен состоять из 16 цифр"),
        ("1234", "Номер карты должен состоять из 16 цифр"),
        ("abcdefghijklmnop", "Номер карты должен состоять из 16 цифр"),
        ("123456781234567890", "Номер карты должен состоять из 16 цифр"),
    ],
)
def test_card_masking_errors(invalid_input: str, expected_error: str) -> None:
    """Проверяем обработку невалидных номеров карт"""
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(invalid_input)
    assert str(exc_info.value) == expected_error