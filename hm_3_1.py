#1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def div(*args):

    try:
        arg1 = int(input('Введите число: '))
        arg2 = int(input('Введите число для деления: '))
        res = arg1 / arg2
    except ValueError:
        return 'Ошибка!'
    except ZeroDivisionError:
        return 'Неверное действие! Ноль нельзя использовать в качестве разделителя.'
    return res
print(f'result  {div()}')
