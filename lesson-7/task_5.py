# Напишите функцию-декоратор my_decorator, в которую можно обернуть функцию, которая принимает один входной параметр.
# Ваш декоратор должен будет выводить в консоль входной параметр оборачиваемой функции, запускать функцию, а затем
# выводить результат этой функции.
# Пример кода программы, использующей ваш декоратор и ожидаемый вывод программы находится комментарии к слайду.


def my_decorator(func):
    def wrap_function(input_arg):
        print('The function accepted an argument: ', input_arg)
        result = func(input_arg)
        print('Result of the function: ', result)
        return result
    return wrap_function


@my_decorator
def any_func(input_arg):
    return input_arg ** 5


result = any_func(5)