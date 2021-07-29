# The game "guess the number"

import random

number_attempts = 10
secret_number = random.randint(0, 100)
print('Отгадайте целое число от 0 до 100, загаданное компьютером')
while True:
    user_number = int(input('Введите число: '))
    if user_number == secret_number:
        print('Вы угадали. Поздравляем!!!')
        break
    elif user_number > secret_number:
        print('Загаданное число меньше введенного')
    else:
        print('Загаданное число больше введенного')
    number_attempts -= 1
    if number_attempts == 0:
        print(f'Попытки исчерпаны. Вы проиграли. Загаданное число {secret_number}')
        break
