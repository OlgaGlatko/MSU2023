import numpy as np
import matplotlib.pyplot as plt
import random

#Генератор случайного набора данных из 200 строк,
#Основанный на равновероятном распредедении величин
def generation_of_data(size):
    
    global x 
    global y 
    x = np.arange(0,size, 1.)
    deviation = np.zeros((size, 1))
    y = np.zeros((size, 1))

    for i in range(size):
        deviation[i] = random.uniform(-5, 5)
        y[i] = x[i] + deviation[i]

    return x, y

size = 200
x_axis, y_axis = generation_of_data(size)

#В этих массивах храним коэффициенты для решения системы
coefficient = np.zeros((2,2))
free_member = np.array([0, 0])

#Считаем коэффициенты по известным формулам
for i in range(size):
    coefficient[0][0] = coefficient[0][0] + x[i]**2
    coefficient[0][1] = coefficient[0][1] + x[i]
    coefficient[1][0] = coefficient[1][0] + x[i]
    coefficient[1][1] = size
    free_member[0] = free_member[0] + x[i]*y[i]
    free_member[1] = free_member[1] + y[i]

#Самый простой способ решить систему из двух линейных уравнений ЛДП!
result = np.linalg.inv (coefficient). dot (free_member)

#считаем значения аппроксимируещей прямой
y_approximate = np.zeros((size, 1))
for i in range(size):
    y_approximate[i] = result[0]*x[i] + result[1]

 
#Строим графики   
plt.plot(x_axis, y_axis, 'o', label = 'Истинные значения')
plt.plot(x_axis, y_approximate, '*', label = 'Аппроксимирующая прямая')
plt.legend(loc = 'best', fontsize=12) 
plt.xlabel('x порядковый номер измерения', fontsize=14)
plt.ylabel('y оценка величины', fontsize=14)




