from functools import wraps
from datetime import datetime


def log(filename=''):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            func_name = func.__name__
            time = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')

            print(f"[LOG][{time}] Начало выполнения функции: {func_name}")
            try:

                result = func(*args, **kwargs)

                print(f"[LOG][{time}] Результат функции: {result}")

                return result

            except Exception as e:
                print(f"[ERROR][{time}] В функции {func_name} возникла ошибка: {e}. Входные параметры: {args}, {kwargs}")

                raise

            finally:
                print(f"[LOG][{time}] Конец выполнения функции: {func_name}")

        return wrapper

    return decorator


# @log()
# def divide(a, b):
#     return a / b
#
#
# divide(10, 0)