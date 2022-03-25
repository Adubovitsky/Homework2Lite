
number=254314
numberstr=str(number)
sumofdig = 0
i=0
while i < len(numberstr):
    sumofdig= sumofdig + int(numberstr[i])
    i = i + 1

print(sumofdig)