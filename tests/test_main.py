from unittest.mock import patch

import pytest

from src.main import main

import io


# @patch("builtins.input", side_effect=["1", "executed", "да", "да", "да", "да", "вкл"])
# def test_main_json(mocked_input):
#     """ Тест главной функции. """
#     main()

# @patch("builtins.input", side_effect=["1", "executed", "да", "да", "да", "да", "вкл"])
# def test_main_json(mocked_input):
#     """Тест главной функции: проверяем, что main() выполнился без исключений."""
#     try:
#         main()
#     except Exception as e:
#         assert False, f"main() вызвал ошибку: {e}"
#     # Если исключение не возникло — тест пройден

@patch("builtins.input", side_effect=["1", "executed", "да", "да", "да", "да", "вкл"])
@patch("sys.stdout", new_callable=io.StringIO)
def test_main_json_with_invalid_data(mocked_input, mocked_stdout):
    """Тест: проверяем обработку ошибки некорректного номера счёта."""
    with pytest.raises(ValueError, match="Нестандартный номер счета"):
        main()

@patch("builtins.input", side_effect=["2", "executed", "да", "да", "да", "да", "вкл"])
@patch("sys.stdout", new_callable=io.StringIO)
def test_main_csv(mocked_input, mocked_stdout):
    """Тест: проверяем обработку ошибки некорректного номера счёта."""
    with pytest.raises(ValueError, match="Нестандартный номер счета"):
        main()




# @patch("builtins.input", side_effect=["2", "canceled", "нет", "да", "да", "да", "вкл"])
# def test_main_csv(mocked_input):
#     """ Тест главной функции. """
#     main()


# @patch("builtins.input", side_effect=["3", "pending", "да", "нет", "да", "да", "вкл"])
# def test_main_xlsx(mocked_input):
#     """ Тест главной функции. """
#     main()
@patch("builtins.input", side_effect=["3", "executed", "да", "да", "да", "да", "вкл"])
@patch("sys.stdout", new_callable=io.StringIO)
def test_main_xlsx(mocked_input, mocked_stdout):
    """Тест: проверяем обработку ошибки некорректного номера счёта."""
    with pytest.raises(ValueError, match="Нестандартный номер счета"):
        main()

@patch("builtins.input", side_effect=["0", "pending", "да", "нет", "да", "да", "вкл"])
def test_main_exit_when_file_choice(mocked_input):
    """ Тест главной функции. """
    main()


@patch("builtins.input", side_effect=["2", "0", "да", "нет", "да", "да", "вкл"])
def test_main_exit_when_status(mocked_input):
    """ Тест главной функции. """
    main()


@patch("builtins.input", side_effect=["1", "executed", "да", "нет", "нет", "да", "ыдвлоапр"])
def test_main_wrong_search(mocked_input):
    """ Тест главной функции. """
    main()