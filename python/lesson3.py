if door_is_closed:  # Если мы  не сравниваем, то он  мы сравниваем с True
    if door_is_locked:
        unlock_door()  # вызов функции
    open_door()
advance()


# Интепритатор Python управление потоками
for n in range(2, 10):
    x_range = range(2, n)
    for x in x_range:
        if n % x == 0:  # ДЕЛЕНИЕ ПО МОДУЛЮ, ОСТАТОК ПО ДЕЛЕНИЮ
            break
    else:
        # loop fell through without finding a factor
        print(n)
print(range())

int()
