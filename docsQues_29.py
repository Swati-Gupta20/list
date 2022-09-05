l=[5, 6, [], 3, [], [], 9]
remove=[]
l2=[]
i=0
while(i<len(l)):
    i+=1
    if l[i-1]==remove:
        continue
    l2.append(l[i-1])
print(l2)



