#Zdanie 1
x=int(input('Введите минусовое число = '))
print(x<0 and x or "МИНУСОВОЕ число же ")

#Zadanie 2
y=int(input('\nВведите ваше число для проверки = '))
print((y < 20 and 'Число действетельно меньше') or 'Число больше' )

# Zadanie 3

x=int(input('\nВведите число для проверки = '))
print(( x == 0 and 'Да ,равно (0)' ) or 'Неравно (0)')

#Zadanie 4
x=int(input('\nВведите число для проверки = '))
print((x%2 == 0 and 'Число чётное') or x%2 != 0 and 'Число нечётное ')

#Zadanie 5
x=(input('\nВвeдите 3 любых  числа через пробел =')).split()
print( int(max(x)))