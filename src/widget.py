from src.masks import get_mask_account, get_mask_card_number
from dateutil.parser import parse


def mask_account_card(pay_info: str) -> str:
    """Обрабатывает информацию о картах и счетах и возвращает строку с замаскированным номером"""
    if not isinstance(pay_info, str) or not pay_info.strip():
        raise ValueError("Некорректный формат данных: ожидается непустая строка.")

    parts = pay_info.split()
    if len(parts) < 2:
        raise ValueError("Строка не содержит нужной информации для обработки")

    # Последний элемент должен быть номером (только цифры)
    number = parts[-1]
    if not number.isdigit():
        raise ValueError("Номер должен содержать только цифры")

    # Все элементы кроме последнего - это название банка/типа
    bank_name = " ".join(parts[:-1])

    try:
        if bank_name == "Счет":
            return f"{bank_name} {get_mask_account(number)}"
        else:
            return f"{bank_name} {get_mask_card_number(number)}"
    except ValueError as e:
        # Перехватываем ошибки из внутренних функций
        raise ValueError(f"Ошибка обработки номера: {str(e)}")


def get_date(date_string: str) -> str:
    """Смена даты с формата ISO на 'ДД.ММ.ГГГГ'"""
    date = parse(date_string)
    formatted_date = date.strftime("%d.%m.%Y")
    return formatted_date


def get_date(date_string: str) -> str:
    """Смена даты с формата ISO на 'ДД.ММ.ГГГГ'"""
    date = parse(date_string)
    formatted_date = date.strftime("%d.%m.%Y")
    return formatted_date


print(get_date("2024-03-11T02:26:18.671407"))

print(mask_account_card("Maestro 1596837868705199"))
print(mask_account_card("Счет 64686473678894779589"))
print(mask_account_card("MasterCard 7158300734726758"))
print(mask_account_card("Счет 35383033474447895560"))
print(mask_account_card("Visa Classic 6831982476737658"))
print(mask_account_card("Visa Platinum 8990922113665229"))
print(mask_account_card("Visa Gold 5999414228426353"))
print(mask_account_card("Счет 73654108430135874305"))
