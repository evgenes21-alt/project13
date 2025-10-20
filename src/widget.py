from dateutil.parser import parse

from src.masks import get_mask_account, get_mask_card_number


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


