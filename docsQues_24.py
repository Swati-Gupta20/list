list = [1,2,3,1,2,2]
l=[]
i=0
while(i<len(list)):
    if list[i] not in l:
        l.append(list[i])
    i+=1
print(l)