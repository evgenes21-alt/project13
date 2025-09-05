# 7000792289606361     # входной аргумент
# 7000 79** **** 6361  # выход функции


def get_mask_card_number(card: int) -> str:
    """Функция которая маскирует номер карты"""
    card_number = str(card)
    card_number = card_number[:6] + "*" * 6 + card_number[-4:]
    card_number = card_number[:4] + " " + card_number[4:8] + " " + card_number[8:12] + " " + card_number[12:]
    return card_number


# 73654108430135874305  # входной аргумент
#               **4305  # выход функции


def get_mask_account(account: int) -> str:
    """Функция которая маскирует номер счёта"""
    card_account = str(account)
    card_account = "**" + card_account[-4:]
    return card_account