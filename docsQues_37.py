l=[1, 2, 3, 4, 5, 6]
l2=[]
i=0
while(i<len(l)-1):
    a=l[i],l[i+1]
    l2.append(list(a))
    i+=1
print(l2)