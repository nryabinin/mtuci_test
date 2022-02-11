# Задача: На вход программе подаются 3 коэффициента квадратного
# уравнения. Программа должна находить корни квадратного уравнения.
from cmath import sqrt

a = int(input())
b = int(input())
c = int(input())

print(f'{b}x^2 + {a}x + c = 0')

D = (pow(b, 2)) - (4 * a * c)
print(f'D = = {D}')

if D < 0:
    print('Нет корней')

if D >= 0:
    x1 = (-b + sqrt(D)) / (2 * a)
    print(f'x1 = {x1}')
if D > 0:
    x2 = (-b - sqrt(D)) / (2 * a)
    print(f'x2 = {x2}')

