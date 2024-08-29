from unittest import mock
import pytest
import tkinter as tk
from gendiff_tk.scripts import main


@pytest.fixture
def diff_app():
    root = tk.Tk()
    app = main.DiffApp(root)
    return app


def test_open_file1(diff_app, monkeypatch):
    mock_file_path = "/path/to/test_file1.txt"
    monkeypatch.setattr('tkinter.filedialog.askopenfilename', lambda *args, **kwargs: mock_file_path)

    diff_app.load_file1()

    assert diff_app.file1_label.cget("text") == 'Файл 1: Загружен'
    assert diff_app.file1 == mock_file_path


def test_open_file2(diff_app, monkeypatch):
    mock_file_path = "/path/to/test_file2.txt"
    monkeypatch.setattr('tkinter.filedialog.askopenfilename', lambda *args, **kwargs: mock_file_path)

    diff_app.load_file2()

    assert diff_app.file2_label.cget("text") == 'Файл 2: Загружен'
    assert diff_app.file2 == mock_file_path


def test_open_file_dialog(diff_app, monkeypatch):
    mock_file_path = "/path/to/test_file.txt"
    monkeypatch.setattr('tkinter.filedialog.askopenfilename', lambda *args, **kwargs: mock_file_path)

    with mock.patch('tkinter.messagebox.showwarning') as mock_showwarning:
        result = diff_app.open_file_dialog("Выберите Файл")
        assert result == mock_file_path
        mock_showwarning.assert_not_called()


def test_open_file_dialog_errors(diff_app, monkeypatch):
    mock_file_path = ""
    monkeypatch.setattr('tkinter.filedialog.askopenfilename', lambda *args, **kwargs: mock_file_path)

    with mock.patch('tkinter.messagebox.showwarning') as mock_showwarning:
        result = diff_app.open_file_dialog("Выберите Файл")
        assert result == mock_file_path
        mock_showwarning.assert_called_once_with("Ошибка", "Вы не выбрали файл.")


def test_update_status(diff_app):
    mock_label = mock.MagicMock(spec=tk.Label)
    test_text = "New Status"
    diff_app.update_status(mock_label, test_text)
    mock_label.config.assert_called_once_with(text=test_text)


# def test_update_diff_success(diff_app, monkeypatch):
#     diff_app.file1 = "tests/fixtures/text1.txt"
#     diff_app.file2 = "tests/fixtures/text2.txt"
#     mock_diff_result = ("diff result\n"
#                         "\n")
#     monkeypatch.setattr('gendiff_tk.gendiff.gendiff', lambda file1, file2: mock_diff_result)
#     with mock.patch.object(diff_app.result_text, 'delete') as mock_delete, \
#             mock.patch.object(diff_app.result_text, 'insert') as mock_insert:
#         diff_app.update_diff()
#
#         mock_delete.assert_called_once_with(1.0, tk.END)
#         mock_insert.assert_called_once_with(tk.END, mock_diff_result)
