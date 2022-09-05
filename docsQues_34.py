

l=[34.67, 12, -94.89, 'Python', 0, 'C#']
l2=[]
i=0
while(i<len(l)):
    if type(l[i])==str:
        l2.append(l[i])
    i+=1
print(l2)

