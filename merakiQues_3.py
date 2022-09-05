# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# len=len(numbers)
# i=0
# max=0
# while(i<len):
#     num=numbers[i]
#     if num>max:
#         max=num
#     i+=1
# print(max)




numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
len=len(numbers)
i=0
max=0
max2=0
while(i<len):
    num=numbers[i]
    if num>max:
        max=num
    elif num<max and num>max2:
        max2=num
    i+=1
print(max2)