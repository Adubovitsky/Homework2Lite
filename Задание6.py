#Задача 6
#Найти сумму цифр числа.

number=254314
numberstr=str(number)
sumofdig = 0

for i in (numberstr):
    sumofdig = sumofdig + int(i)

print(sumofdig)