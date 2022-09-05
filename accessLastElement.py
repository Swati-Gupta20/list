l=[[7,1], [8, 3], [5, 7], [9, 11], [13, 15, 17]]
l2=[]
i=0
while(i<len(l)):
    size2=len(l[i])
    a=l[i][size2-1]
    l2.append(a)
    i+=1
print(l2)
