number=354359688
numberstr=str(number)
max=0
i=0
for i in range(len(numberstr)):
    if  int(numberstr[i])>max:
        max= int(numberstr[i])

print(max)


