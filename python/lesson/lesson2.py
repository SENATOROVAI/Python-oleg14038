# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: base
#     language: python
#     name: python3
# ---

# +
"""Модуль для поиска наибольшего значения в списке чисел."""

number_max = [1, 2, 3]  # список - Структура данных

# алгоритм поиска наибольшего значения
# Алгоритм = последовательность действий, для выполнения задачи

max_value = number_max[0]  # Создали новую переменную max_value
# и присвоили ей значение элемента с индексом ноль

for number in number_max:  # in оператор членства
    max_value = max(max_value, number)  # Используем встроенную
    # функцию max для обновления max_value

print(max_value)  # Максимальный элемент
# -

# ### Алгоритм - написание калькулятор
# ### 1) Ввести число
# ### 2) Действие
# ### 3) Ввести второе число
# ### 4) вывести результат

# +
operation_list = ["+", "-", "/", "*"]


def calculate(num_1: float, math_: str, num_2: float) -> int | float:
    """Выполняет математическую операцию с.

    двумя числами и выводит результат на консоль.

    Параметры.
    num_1 (float): Первое число.
    math_ (str): Математическая операция (+, -, /, *).
    num_2 (float): Второе число.

    Возвращает:
    float: Результат вычислений. Если произошла ошибка, возвращает 0.0.
    """
    try:
        if math_ == "/" and num_2 == 0:
            print("Error: Division by zero")
            return 0.0

        if math_ == "+":
            result = num_1 + num_2
        elif math_ == "-":
            result = num_1 - num_2
        elif math_ == "/":
            result = num_1 / num_2
            result = int(result) if result.is_integer() else result
        elif math_ == "*":
            result = num_1 * num_2
        else:
            print("Unknown operation")
            return 0.0

        print(f"{num_1} {math_} {num_2} = {result}")
        return result

    except ValueError:
        print("Error: Invalid input data")
        return 0.0


def is_input_valid(number_one: str, opr: str, number_two: str) -> bool:
    """Проверяет корректность входных данных.

    Параметры:
    number_one (str): Первое число в строковом формате.
    opr (str): Математическая операция (+, -, /, *).
    number_two (str): Второе число в строковом формате.

    Возвращает:
    bool: True если данные корректны, иначе False.
    """
    if opr not in operation_list:
        print("Error: Invalid operation")
        return False

    try:
        float(number_one)
        float(number_two)
        return True
    except ValueError:
        print("Error: Invalid number format")
        return False
