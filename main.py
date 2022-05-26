#Zadanie 1
import math

print('Hello World')
a = 'Home'
print(a)
print("Work")
print("Hello World , Home Work") #Хотел вывести через переменную (а) , но не понял как (

#Zadanie 2
b= input('Ввeдите длину прямоугольник = ')
c =input('Введите ширину прямогульника =')
L = int(b)*int(c)
print('Площадь промоугольника = ' ,int(L))

#Zadanie 3
q = input('\nВвeдите первое число = ')
w = input('Ввeдите второе число = ')

print('\nSuma = ',int(q)+int(w),
      '\nProiwodnoe = ',int(q)*int(w),
      '\nRazdost = ', float(q)/float(w),  #Дал float чтобы в случае чего , видно было дроби
      '\nChastnost = ', float(q)%float(w))

#Zadanie 4

r = input('\nРадиус круга = ' )
D = int(r)*int(r)
L = int(r)*math.pi
A = int(r)++2*math.pi
print('Radius = ',int(r),
      '\nDiametr = ', int(D),
      '\nDlina = ', float(L),
      '\nPlozhat = ', float(A))