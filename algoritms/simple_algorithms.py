"""
Module with functions for performing basic algorithmic tasks and operations:
- Checking a prime number
- The sum of the digits of the number
- Squares of the numbers in the list
- Removing duplicate characters and spaces from a string
- Counting words per line
- Lucky Number Calculator
"""


def is_prime_number():
    """Определить, является ли введенное число простым.

    Простое число делится только на себя и на 1.
    """
    number = int(input("Введите число: "))

    divisor_count = 0  # Количество делителей
    divisors = []

    for num in range(1, number + 1):  # Перебираем числа от
        # до number включительно
        if number % num == 0:
            divisor_count += 1
            divisors.append(num)
    if divisor_count == 2:  # Если количество делителей равно 2, число простое
        print("Число простое")
    else:
        print("Число непростое")
        print(divisors)  # Выводим все делители числа


def sum_of_digits():
    """Найти сумму цифр введенного числа."""
    num = int(input("Введите число: "))
    sum_digits = 0

    while num > 0:  # Пока число больше 0
        sum_digits += num % 10  # Добавляем последнюю цифру числа к сумме
        num //= 10  # Удаляем последнюю цифру числа
    print(sum_digits)


def square_numbers():
    """Преобразовать список чисел в список квадратов этих чисел."""
    numbers = [4, 5, 6, 7]
    squared_numbers = []

    for number in numbers:
        squared_numbers.append(number**2)
    print(squared_numbers)

    # Используем генератор списков
    numbers_2 = [4, 5, 6]
    squared_numbers_2 = [x**2 for x in numbers_2]
    print(squared_numbers_2)


def remove_duplicates_and_spaces():
    """Удалить из строки повторяющиеся символы и все пробелы."""
    input_string = input("Введите строку: ")
    unique_chars = ""

    for char in input_string:
        # Если символа нет в новой строке и он не является пробелом
        if char not in unique_chars and char != " ":
            unique_chars += char
    print(unique_chars)


def count_words():
    """Подсчитать количество слов в строке, разделенных пробелами."""
    input_sentence = input("Введите строку: ")
    word_count = 0
    for char in input_sentence:
        if char == " ":
            word_count += 1
    print(word_count + 1)

    # Альтернативный метод с использованием split
    input_sentence_2 = input("Введите строку: ")
    print(len(input_sentence_2.split()))  #


def lucky_number_calculator():
    """Создать калькулятор счастливых чисел."""
    birth_date = input("Введите дату рождения в формате ДД.ММ.ГГ: ")

    # Разделяем дату на день, месяц и год
    birth_date_parts = birth_date.split(".")
    day = int(birth_date_parts[0])
    month = int(birth_date_parts[1])
    year = int(birth_date_parts[2])
    sum_birth_date_digits = 0

    # Считаем сумму цифр дня
    while day > 0:
        sum_birth_date_digits += day % 10
        day //= 10

    # Считаем сумму цифр месяца
    while month > 0:
        sum_birth_date_digits += month % 10
        month //= 10

    # Считаем сумму цифр года
    while year > 0:
        sum_birth_date_digits += year % 10
        year //= 10

    print("Сумма цифр вашей даты рождения:", sum_birth_date_digits)


# Вызов функций для демонстрации
is_prime_number()
sum_of_digits()
square_numbers()
remove_duplicates_and_spaces()
count_words()
lucky_number_calculator()
