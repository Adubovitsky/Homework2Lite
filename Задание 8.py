number=input('Введите число')
result=''
i=0
for i in range(len(number)):
    if int(number[i])==5:
        result= 'Цифра 5 есть в числе'
    else:
        result='Цифры 5 нет в числе'
print(result)