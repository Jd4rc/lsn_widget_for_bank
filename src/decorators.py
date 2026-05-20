from functools import wraps

def log(filename=''):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            func_name = func.__name__

            print(f"[LOG] Начало выполнения функции: {func_name}")
            try:

                result = func(*args, **kwargs)

                print(f"[LOG]Результат функции: {result}")

                return result

            except Exception as e:
                print(f"[ERROR] В функции {func_name} возникла ошибка: {e}")


            print(f"[LOG] Конец выполнения функции: {func_name}")

        return wrapper

    return decorator