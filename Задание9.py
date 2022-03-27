# Задача 9
# Найти максимальную цифру в числе

number=354359688
numberstr=str(number)
max=0

for i in numberstr:
    if int(i)>max: max=int(i)

print(max)


