number=354359688555555555
numberstr=str(number)
countoffive=0

for i in range(len(numberstr)):
    if int(numberstr[i])==5:
        countoffive=countoffive+1

print(countoffive)

