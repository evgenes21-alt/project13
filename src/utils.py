import json
import logging
import os
from json import JSONDecodeError

from src.external_api import convert_curr

dir_path = os.path.dirname(os.path.realpath(__file__))
logs_path = os.path.join(dir_path, "..", "logs", "utils.log")

utils_logger = logging.getLogger("utils")
file_handler = logging.FileHandler(logs_path, "a", encoding="UTF-8")
file_formatter = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
utils_logger.addHandler(file_handler)
utils_logger.setLevel(logging.DEBUG)


def converted_transactions(json_path: str) -> list:
    """Функция преобразует входящий json объект в список словарей"""

    try:
        utils_logger.info("Попытка прочитать файл json")
        with open(json_path, encoding="utf-8") as data:
            transaction_data = data.read()
            utils_logger.info("Чтение и обработка файла успешна")
        return json.loads(transaction_data)
    except FileNotFoundError:
        utils_logger.error("Файл не найден")
        print("Файл не найден")
        return []
    except JSONDecodeError:
        utils_logger.error("Произошла ошибка при декодировании файла json")
        return []


def transaction_amount(transaction: dict) -> int:
    """
    Функция возвращает сумму транзакции в рублях.
    Если транзакция была в USD или EUR, происходит обращение к внешнему API
    для получения текущего курса валют и конвертации суммы операции в рубли.
    """

    trans_curr = transaction["operationAmount"]["currency"]["code"]
    trans_amount = transaction["operationAmount"]["amount"]
    result = trans_amount
    utils_logger.info(f"Принята транзакция на обработку, валюта {trans_curr}")

    # ecли валюта транзакции не рубль, то обращение к API для конвертации
    if trans_curr != "RUB":
        result = convert_curr(trans_curr, "RUB", trans_amount)
        trans_curr = "RUB"
        utils_logger.info("Конвертация валюты успешна, возвращена сумма в рублях")

        if result == -1:
            trans_curr = transaction["operationAmount"]["currency"]["code"]
            result = transaction["operationAmount"]["amount"]
            utils_logger.warning(
                "Конвертация не удалась, сумма возвращена в исходной валюте"
            )

    return result
