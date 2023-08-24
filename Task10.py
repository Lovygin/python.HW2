'''
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть
'''
import random
coins = int(input('Enter number of coins: '))
events = ['o', 'r'] # список из случаев, из которго будет составлена рандомная строка случаев
random_string = ''.join(random.choice(events) for _ in range(coins)) #создаем рандомное расположение монет на столе
print(random_string)
r = random_string.count('r')
o = random_string.count('o')
if  r > o:
    print(f'You need to flip {o} coins with an eagle') # Нужно перевернуть n монет с орлом
else: print(f'You need to flip {r} coins with tails') # tails - решка