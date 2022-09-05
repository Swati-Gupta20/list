numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
len=len(numbers)
count=0
i=0
while(i<len):
    num=numbers[i]
    if (num>20 and num<40):
        count+=1
    i+=1
print(count)