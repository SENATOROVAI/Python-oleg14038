from addition import add
from multiplication import mult
from run import get_input_data
from subtraction import sub

# comment
while True:
    try:
        num, operator, num2 = get_input_data()
        if operator == "+":
            print("Результат операции:", add(num, num2))
        elif operator == "-":
            print("Результат операции:", sub(num, num2))
        elif operator == "*":
            print("Результат операции:", mult(num, num2))
        else:
            print("Ошибка! Некорректный оператор.")

    except ValueError:
        print("Ошибка, введите правильное значение")
