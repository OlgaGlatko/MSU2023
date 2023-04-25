from sympy import * #Библиотека для работы с многочленами. ЛДП!
import pandas as pd
import numpy as np

#В функции считаются слагаемые суммы 
def basic_polinom(x_v, y_v, k):
    Numerator = ''
    Denominator = 1
    for j in range(len(x_value)):
        if k != j:
            #Собираем числитель в виде строки для каждого x[i]
            Numerator += ('(x -' + str(x_value[j]) + ')*') 
            #Собираем знаменатель
            Denominator *= (x_v - x_value[j]) 
    #В виде строки возвращаем для x[i] кусок многочлена        
    return (str(y_v/Denominator)) +'*'+ Numerator

#Блок инициализации переменных
ch = '*' 
polinom = ''
file_encoding_in = 'UTF8' 

#Для простоты проверки работы кода предалагется просто пример:
Data = pd.read_csv('Data2.csv', sep=';', decimal=',', encoding=file_encoding_in) 
Data = Data. dropna()
Data = Data[Data.Pres > 0].reset_index(drop=True)

x_value = Data['Salinity']
y_value = Data['Pres']


#Высов функции
for i in range(len(x_value)):
    #Метод rstrip отрезает последний значок *. Если его оставить,
    #функция expand не будет работать.
    basic_polinoms = basic_polinom(x_value[i], y_value[i], i).rstrip(ch)    
    polinom += ' +' +  basic_polinoms #Собираем в виде строки сам многолен

#Функция expand упрощает выражения в виде: (x-1)*(x+1)+(x-5)*(x+6)*(x-6)
print(expand(polinom))
    


            


