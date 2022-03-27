# Задача 7
# Найти произведение цифр числа.

number=254314
numberstr=str(number)
productofdig = 1

for i in numberstr:
    productofdig=productofdig*int(i)

print(productofdig)