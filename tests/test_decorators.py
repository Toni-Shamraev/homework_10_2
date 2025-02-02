from src.decorators import my_function, log


def test_my_function_success(capsys):
    result = my_function(3, 4)
    assert result == 7
    captured = capsys.readouterr()
    assert "Начало работы функции: my_function, с параметрами 3 и 4" in captured.out
    assert "Функция my_function выполнена успешно с результатом: 7" in captured.out


def test_my_function_fail(capsys):
    @log
    def my_function(x, y):
        return x / y
    result = my_function(5, 0)
    assert result is None
    captured = capsys.readouterr()
    assert "Начало работы функции: my_function, с параметрами 5 и 0" in captured.out
    assert "Функция my_function завершилась с ошибкой" in captured.out
