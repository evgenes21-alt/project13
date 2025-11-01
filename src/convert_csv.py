import csv
import logging
import os

import pandas as pd

dir_path = os.path.dirname(os.path.realpath(__file__))
logs_path = os.path.join(dir_path, "..", "logs", "convert.log")

operations_logger = logging.getLogger("operations")
file_handler = logging.FileHandler(logs_path, "w", encoding="UTF-8")
file_formatter = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
operations_logger.addHandler(file_handler)
operations_logger.setLevel(logging.DEBUG)


def read_from_csv(file_path: str) -> list[dict]:
    """Функция принимает пусть к файлу .csv и возвращает список словарей."""
    try:
        with open(file_path, encoding="utf-8") as file_name:
            reader = csv.DictReader(file_name, delimiter=";")

            operations_logger.info(f"Успешное чтение файла {file_path}")
            return list(reader)
    except FileNotFoundError as e:
        operations_logger.error(f"Ошибка чтения файла {file_path} {e}")
        return []


def read_from_excel(file_path) -> list[dict]:
    """Функция принимает путь к файлу формата excel и возвращает список словарей."""
    try:
        excel_data = pd.read_excel(file_path).to_dict(orient="records")
        operations_logger.info(f"Успешное чтение файла {file_path}")
        return excel_data
    except FileNotFoundError:
        operations_logger.error(f"Ошибка чтения файла {file_path}")
        return []
result_csv = read_from_csv('path/to/your/file.csv')
print(result_csv)

result_excel = read_from_excel('path/to/your/file.xlsx')
print(result_excel)

if __name__ == "__main__":
    # Тестируем чтение CSV
    csv_file_path = "transactions.csv"  # Укажите реальный путь к вашему CSV файлу
    csv_data = read_from_csv(csv_file_path)
    print("\nДанные из CSV:")
    for row in csv_data[:5]:  # Выводим первые 5 строк
        print(row)

    # Тестируем чтение Excel
    excel_file_path = "transactions_excel.xlsx"  # Укажите реальный путь к вашему Excel файлу
    excel_data = read_from_excel(excel_file_path)
    print("\n\nДанные из Excel:")
    for row in excel_data[:5]:  # Выводим первые 5 строк
        print(row)