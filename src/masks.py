# 7000792289606361     # входной аргумент
# 7000 79** **** 6361  # выход функции

import logging
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
logs_path = os.path.join(dir_path, "..", "logs", "utils.log")

masks_logger = logging.getLogger("masks")
file_handler = logging.FileHandler(logs_path, "w", encoding="UTF-8")
file_formatter = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
masks_logger.addHandler(file_handler)
masks_logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """Функция которая маскирует номер карты"""
    if card_number is None:
        error_msg = "Номер карты не может быть None"
        raise ValueError(error_msg)

    if (len(card_number)) != 16 or not card_number.isdigit():
        error_msg = "Номер карты должен состоять из 16 цифр"
        raise ValueError(error_msg)

    card_number = card_number[:6] + "*" * 6 + card_number[-4:]
    card_number = (
        card_number[:4]
        + " "
        + card_number[4:8]
        + " "
        + card_number[8:12]
        + " "
        + card_number[12:]
    )
    return card_number


# 73654108430135874305  # входной аргумент
#               **4305  # выход функции


def get_mask_account(account: str) -> str:
    """Функция которая маскирует номер счёта"""
    card_account = str(account)
    card_account = "**" + card_account[-4:]
    return card_account
