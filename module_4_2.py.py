def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()
#При выносе вызова функции inner_function() будет ошибка т.к. она не находится
# в объемлющей видимости функции test_function


test_function()