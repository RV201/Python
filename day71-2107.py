numberList = [15, 85, 125, 89, 125]

minNum = numberList[0]
for num in numberList:
    if minNum < num:
        minNum = num
print(minNum)