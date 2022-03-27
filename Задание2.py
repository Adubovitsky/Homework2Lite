# Задача 2
# Пользователь в цикле вводит 10 производных цифр. Выведите количество введеных пользователем цифр 5.

sumoffive = 0

for i in range(10):
    number=int(input("Введите целое число "))
    if number==5: sumoffive = sumoffive+1
print(sumoffive)


