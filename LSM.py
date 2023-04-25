import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


file_encoding_in = 'UTF8' 

Data = pd.read_csv('Data.csv', sep=';', decimal=',', encoding=file_encoding_in)
x_axis = Data['x']
y_axis = Data['y']
size = len(x_axis)


#В этих массивах храним коэффициенты для решения системы
coefficient = np.zeros((2,2))
free_member = np.array([0, 0])

#Считаем коэффициенты по известным формулам
for i in range(size):
    coefficient[0][0] = coefficient[0][0] + x_axis[i]**2
    coefficient[0][1] = coefficient[0][1] + x_axis[i]
    coefficient[1][0] = coefficient[1][0] + x_axis[i]
    coefficient[1][1] = size
    free_member[0] = free_member[0] + x_axis[i]*y_axis[i]
    free_member[1] = free_member[1] + y_axis[i]

#Решаем систему из двух линейных уравнений ЛДП!
result = np.linalg.inv (coefficient). dot (free_member)

#считаем значения аппроксимируещей прямой
y_approximate = np.zeros((size, 1))
for i in range(size):
    y_approximate[i] = result[0]*x_axis[i] + result[1]

 
#Строим графики    
plt.plot(x_axis, y_axis, 'o', label = 'Истинные значения')
plt.plot(x_axis, y_approximate, '*', label = 'Аппроксимирующая прямая')
plt.legend(loc = 'best', fontsize=12) 
plt.xlabel('x порядковый номер измерения', fontsize=14)
plt.ylabel('y оценка величины', fontsize=14)




