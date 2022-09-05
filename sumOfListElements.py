# l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# sum=0
# i=0
# while(i<len(l)):
#     sum=sum+l[i]
#     i+=1
# print(sum)


# nested list

l=[[7,1], [8, 3], [5, 7], [9, 11], [13, 15, 17]]
l2=[]
i=0
while(i<len(l)):
    j=0
    sum=0
    size2=len(l[i])
    while(j<size2):
        sum=sum+l[i][j]
        j+=1
    l2.append(sum)
    i+=1
print(l2)