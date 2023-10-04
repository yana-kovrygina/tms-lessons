# Решите прошлую задачу так, чтобы ваш декоратор работал для любой функции, с любым количеством параметров. А также
# чтобы работало с именованными параметрами.
# Подсказка: используйте *args и **kwargs.

def my_decorator(func):
    def wrap_function(*args, **kwargs):
        print("The function accepted arguments: ", args, kwargs)
        result = func(*args, **kwargs)
        print("Result of the function: ", result)
        return result
    return wrap_function


@my_decorator
def messy_func(a, b, c, d, e):
    return a ** 2, b ** 3, c ** 4, (d * 2).upper(), [i * 2 for i in e]


result = messy_func(1, 2, c=3, d='a', e=(4, 5))