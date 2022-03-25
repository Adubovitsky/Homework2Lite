number=254314
numberstr=str(number)
productofdig = 1
i=0
while i < len(numberstr):
    productofdig = productofdig * int(numberstr[i])
    i = i + 1

print(productofdig)