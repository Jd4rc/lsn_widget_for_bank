from functools import wraps

def log(filename=''):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[LOG] Начало выполнения функции: {func.__name__}")

            result = func(*args, **kwargs)

            print(f"[LOG] Конец выполнения функции: {func.__name__}")

            return result
        return wrapper
    return decorator