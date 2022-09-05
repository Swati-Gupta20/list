l=[1,1,2,3,4,5,1,2]
remove=1
l2=[]
i=0
while(i<len(l)):
    i+=1
    if l[i-1]==remove:
        continue
    l2.append(l[i-1])
print(l2)




