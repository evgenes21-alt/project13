from src.masks import get_mask_account, get_mask_card_number
from dateutil.parser import parse




# Пример функции для определения типа карты

def get_card_type(card_number: str) -> str:
    if card_number.startswith("4"):
        return "Visa"
    elif card_number.startswith("5"):
        return "MasterCard"
    elif card_number.startswith("6"):
        return "Discover"
    elif card_number.startswith("3") and (card_number[1] in "47"):
        return "American Express"
    elif card_number.startswith("3"):
        return "JCB"
    elif card_number.startswith("2"):
        return "Maestro"
    else:
        return "Unknown"



def mask_account_card(pay_info: str) -> str:
    """Обрабатывает информацию о картах и счетах и возвращает строку с замаскированным номером"""
    if not isinstance(pay_info, str) or not pay_info.strip():
        raise ValueError("Некорректный формат данных: ожидается непустая строка.")

    parts = pay_info.split()
    if len(parts) < 2:
        raise ValueError("Строка не содержит нужной информации для обработки")

    account = "Счет"
    number = parts[-1]

    try:
        if parts[0] == account:
            return get_mask_account(number)
        else:
            # добавляем определение типа карты
            card_type = get_card_type(number)
            return f"{card_type} {get_mask_card_number(number)}"
    except ValueError as e:
        # Перехватываем ошибки из внутренних функций
        raise ValueError(f"Ошибка обработки номера: {str(e)}")


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
