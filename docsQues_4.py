l=[6,1,3,5,6,3,1]
l2=[]
i=0
while(i<len(l)):
    if l[i] not in l2:
        l2.append(l[i])
    j=0
    p=1
    while(j<len(l2)):
        p=p*l2[j]
        j+=1
    i+=1
print(l2)

