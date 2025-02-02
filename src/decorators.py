from functools import wraps


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Начало работы функции: {func.__name__}, с параметрами {args[0]} и {args[1]}")
        try:
            result = func(*args, **kwargs)
            print(f"Функция {func.__name__} выполнена успешно с результатом {result}")
            return result
        except Exception:
            print(f"Функция {func.__name__} завершилась с ошибкой")

    return wrapper


@log
def my_function(x, y):
    return x + y

my_function(1, 2)

if __name__ == '__main__':
    print(my_function)