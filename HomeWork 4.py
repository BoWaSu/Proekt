#Zadanie 1
import math
try:
    i = int(input("Номер квартиры = "))
    if 36 >= i > 0:
        print(f"Квартира {i} находится в первом подьезде {math.ceil(i/4)} этаж")
    elif 72 >= i > 36:
        print(f"Квартира {i} находится во втором подьезде {math.ceil(i/4 - 9)} этаж")
    elif 108 >= i > 7:
        print(f"Квартира {i} находится в третьем  подьезде {math.ceil(i/4 - 18)} этаж")
    elif 144 >= i > 108:
        print(f"Квартира {i} находится в четвёртом  подьезде {math.ceil(i / 4 - 27)} этаж")
    else:
        print("Данной квартиры нет в доме")
except ValueError:
    print("Это не число  вообще")

#Zadania 2

year = int(input("\nВведите ГОД для проверки = "))
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print('YES')
else:
    print('NO')
print("Спасибо . хорошего дня =)")



#Zadanie 3
try:
    a, d, c = map(int, input("\nВведите три числа через пробел ").split())
    if (a + d > c) or (a + c > d) or (d + c > a):
        print("Треугольник будет существовать")
    else:
        print("Невохможно посторить треугольник")
except ValueError:
    print("Введите числа ")









