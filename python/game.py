import random, sys

print('Камень, Ножницы, Бумага')

#В этих переменных накапливается количкство 
# Побед, поражений и ничьих 

wins = 0 
losses = 0 
ties = 0 

while True:# главный цикл игры
    print('%sпобед, %sпоражений, %sничьих' %(wins, losses, ties))

    while True:
        print('Выберите ход: (к)амень, (н)ожнецы,' '(б)умага или' \
            '(в)ыход')
    playerMove = input('Вв')

print('Камень, Ножницы, Бумага')

#В этих переменных накапливается количкство 
# Побед, поражений и ничьих 

wins = 0 
losses = 0 
ties = 0 

while True:# главный цикл игры
    print('%sпобед, %sпоражений, %sничьих' %(wins, losses, ties))

    while True:
        print('Выберите ход: (к)амень, (н)ожнецы,' '(б)умага или' \
            '(в)ыход')
    playerMove = input()
    if playerMove == 'в':
        sys.exit() #выход из программы 
    if playerMove == 'к' or playerMove == 'н' or playerMove == 'б':
        break #ВЫХОД ИЗ ЦИКЛА ВЫБОРА ХОДА 
    print('Введите "к", "н", "б" или "в" ')

# Отображение выбора пользователя
if playerMove == 'к':
    print('Камень....')
elif playerMove == 'н':
    print('Ножницы....')
elif playerMove == 'б':
    print('БУМАГА и ...')  

# Отображение выбора компьютера
гandomNumber = random.randint(1, 3)
if randomNuber == 1:
    computerMove = 'к'
    print("Камень")
if randomNuber == 2: 
    computerMove = 'н'
    print('Ножницы ')
elif randomNumber == 3:
    computerMove = '6'
    print('БУМАГА')

    if playerMove == 'в':
        sys.exit() #выход из программы 
    if playerMove == 'к' or playerMove == 'н' or playerMove == 'б':
        break #ВЫХОД ИЗ ЦИКЛА ВЫБОРА ХОДА 
    print('Введите "к", "н", "б" или "в" ')

# Отображение выбора пользователя
if playerMove == 'к':
    print('Камень....')
elif playerMove == 'н':
    print('Ножницы....')
elif playerMove == 'б':
    print('БУМАГА и ...')  

# Отображение выбора компьютера
гandomNumber = random.randint(1, 3)
if randomNuber == 1:
    computerMove = 'к'
    print("Камень")
if randomNuber == 2: 
    computerMove = 'н'
    print('Ножницы ')
elif randomNumber == 3:
    computerMove = '6'
    print('БУМАГА')

