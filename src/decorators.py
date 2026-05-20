from datetime import datetime
from functools import wraps
from pathlib import Path


def log(filename=""):
    """
       Декоратор для логирования выполнения функции.

       Логирует:
       - начало выполнения функции,
       - результат выполнения функции,
       - возникшие исключения,
       - завершение выполнения функции.

       Если передан параметр filename,
       логи записываются в текстовый файл внутри директории data/.
       Если директория data отсутствует, она будет создана автоматически.

       При отсутствии filename логи выводятся в консоль.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            func_name = func.__name__
            time = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")

            def write_log(message: str):

                if filename:
                    BASE_DIR = Path(__file__).resolve().parent.parent
                    data_dir = BASE_DIR / "data"
                    data_dir.mkdir(exist_ok=True)
                    log_file = data_dir / filename

                    with open(log_file, "a", encoding="UTF-8") as f:
                        f.write(message + "\n")

                else:
                    print(message)

            write_log(f"[LOG][{time}] " f"Начало выполнения функции: {func_name}")

            try:

                result = func(*args, **kwargs)

                write_log(f"[LOG][{time}] " f"Результат функции: {result}")

                return result

            except Exception as e:
                write_log(
                    f"[ERROR][{time}] "
                    f"В функции {func_name} возникла ошибка: {e}. "
                    f"Входные параметры: {args}, {kwargs}"
                )

                raise

            finally:
                write_log(f"[LOG][{time}] " f"Конец выполнения функции: {func_name}")

        return wrapper

    return decorator


# @log(filename='test.txt')
# def divide(a, b):
#     return a / b
#
#
# divide(10, 0)
