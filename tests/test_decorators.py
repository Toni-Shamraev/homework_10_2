from src.decorators import my_function, log


def test_my_function():
    assert my_function(3, 4) == 7

def test_log_in_file():
    with open("mylog.txt", 'r', encoding='utf-8') as log_file:
        logs = log_file.read()
        assert "Начало работы функции: my_function" in logs
        assert "my_function ok" in logs

