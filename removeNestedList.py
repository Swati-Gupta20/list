l=[[7,1], [8, 3], [5, 7], [9, 11], [13, 15, 17]]
l2=[]
i=0
while(i<len(l)):
    j=0
    sum=0
    size2=len(l[i])
    while(j<size2):
        sum=l[i][j]
        l2.append(sum)

        j+=1
    i+=1
print(l2)