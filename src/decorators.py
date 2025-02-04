from functools import wraps


def log(filename):
    """Декоратор для записи начала работы функции и её результат в текстовый файл mylog"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with open(filename, 'w', encoding='utf-8') as log_file:
                log_file.write(f"Начало работы функции: {func.__name__}, с параметрами {args[0]} и {args[1]}\n")
                try:
                    result = func(*args, **kwargs)
                    log_file.write(f"{func.__name__} ok")
                    return result
                except Exception as error:
                    log_file.write(f"{func.__name__} {str(error)}. Inputs: {args[0]} и {args[1]}")
        return wrapper
    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


my_function(1, 2)

if __name__ == '__main__':
    print(my_function)
