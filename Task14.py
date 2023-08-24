'''
Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
'''
n = int(input('Enter number for output delimiter: ')) # output delimiter - ограничитель вывода
i = 1
while 2**i <= n:
    print(f'2 to the power {i:>2} = {2**i:<4}')
    i += 1