from sympy import * #Библиотека для работы с многочленами. ЛДП!

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

#Блок ввода
#Можно попросить пользователя ввести многочлен, можно считывать с файла
#Пример чтения с файла 
#biks_in = pd.read_csv(LSP, sep=';', decimal=',', ansi)

#Для простоты проверки работы кода возьмем пример:
x_value = [1, 2, 3, 4]
y_value = [1, 2, 3, 4]


#Вызов функции
for i in range(len(x_value)):
    #Метод rstrip отрезает последний значок *. Если его оставить,
    #функция expand не будет работать.
    basic_polinoms = basic_polinom(x_value[i], y_value[i], i).rstrip(ch)    
    polinom += ' +' +  basic_polinoms #Собираем в виде строки сам многочлен

#Функция expand упрощает выражения в виде: (x-1)*(x+1)+ (x-5)*(x+6)*(x-6)
print(expand(polinom))
    


            


