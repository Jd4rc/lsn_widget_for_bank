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


def test_log_raises_exception_and_logs_it(capsys):
    @log()
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    captured = capsys.readouterr()

    assert "[ERROR]" in captured.out
    assert "В функции divide возникла ошибка" in captured.out
    assert "division by zero" in captured.out
    assert "Входные параметры: (10, 0), {}" in captured.out
    assert "Конец выполнения функции: divide" in captured.out
