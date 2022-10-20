<<<<<<< Updated upstream
def my_input():
    l = list()
    n = int(input("Количество входных списков: "))
    while n > 0:
        l.append(input('Элементы списка через пробел: ').split(' '))
        n -=1
    return l
=======
from lib import repeat

l = list()
n = int(input('Количество входных списков: '))
while n > 0:
    l.append(input('Элементы списка через пробел: ').split(' '))
    n -=1
repeat(l)
>>>>>>> Stashed changes
