from masks import get_mask_account
from masks import get_mask_card_number


def mask_account_card(card_type_number: str) -> str:
    """Функция, которая умеет обрабатывать информацию как о картах, так и о счетах"""
    card_info = card_type_number.rsplit(" ", 1)
    if not card_info[0].startswith("Счет"):
        masked_number = get_mask_card_number(int(card_info[1]))
        return f"{card_info[0]} {masked_number}"
    else:
        masked_account = get_mask_account(int(card_info[1]))
        return f"{card_info[0]} {masked_account}"


def get_date(date: str) -> str:
    """Функция, которая возвращает строку с датой в формате "ДД.ММ.ГГГГ"""
    dates = str(date)
    dates = dates[8:10] + "." + dates[5:7] + "." + dates[:4]
    return dates


print(get_date("2024-03-11T02:26:18.671407"))

print(mask_account_card("Maestro 1596837868705199"))
print(mask_account_card("Счет 64686473678894779589"))
print(mask_account_card("MasterCard 7158300734726758"))
print(mask_account_card("Счет 35383033474447895560"))
print(mask_account_card("Visa Classic 6831982476737658"))
print(mask_account_card("Visa Platinum 8990922113665229"))
print(mask_account_card("Visa Gold 5999414228426353"))
print(mask_account_card("Счет 73654108430135874305"))
