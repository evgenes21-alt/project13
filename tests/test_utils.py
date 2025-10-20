from unittest.mock import mock_open, patch

from src.utils import converted_transactions, transaction_amount


@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data='[{"amount": 100, "currency": "USD"}]',
)
def test_valid_file(mock_file):
    """Тест на корректный файл с транзакциями."""
    transactions = converted_transactions("data/operations.json")
    assert transactions == [{"amount": 100, "currency": "USD"}]


@patch("builtins.open", new_callable=mock_open, read_data="")
def test_empty_file(mock_file):
    """Тест на пустой файл."""
    transactions = converted_transactions("data/operations.json")
    assert transactions == []


@patch("builtins.open", side_effect=FileNotFoundError)
def test_file_not_found(mock_file):
    """Тест на случай, если файл не найден."""
    transactions = converted_transactions("data/operations.json")
    assert transactions == []


def test_transaction_amount_rub(some_transaction_rub):
    """Тест на получение суммы в рублях, если транзакция в рублях."""
    assert transaction_amount(some_transaction_rub) == "9824.07"


@patch("src.utils.convert_curr")
def test_transaction_amount_non_rub_success(mock_convert_curr, some_transaction_usd):
    """Тест на получение суммы в рублях, если транзакция в иностранной валюте и запрос успешный."""
    mock_convert_curr.return_value = 158388.33
    result = transaction_amount(some_transaction_usd)
    assert result == 158388.33
    mock_convert_curr.assert_called_once_with("USD", "RUB", "1500.6")


@patch("src.utils.convert_curr")
def test_transaction_amount_non_rub_fail(mock_convert_curr, some_transaction_usd):
    """Тест на получение суммы в рублях, если транзакция в иностранной валюте и запрос провален."""
    mock_convert_curr.return_value = -1
    result = transaction_amount(some_transaction_usd)
    assert result == "1500.6"
