# Задача 10
# Найти количество цифр 5 в числе

number=3543596885555555
numberstr=str(number)
count_five=0

for i in numberstr:
    if int(i)==5:
        count_five=count_five+1

print(count_five)

