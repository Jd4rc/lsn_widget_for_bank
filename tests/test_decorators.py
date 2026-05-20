import pytest

from src.decorators import log



def test_log_returns_function_result(capsys):
    @log()
    def add(a, b):
        return a + b

    result = add(2, 3)

    captured = capsys.readouterr()

    assert result == 5
    assert "[LOG]" in captured.out
    assert "Начало выполнения функции: add" in captured.out
    assert "Результат функции: 5" in captured.out
    assert "Конец выполнения функции: add" in captured.out
