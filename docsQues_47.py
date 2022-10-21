a=['Red', 'Maroon', 'Yellow', 'Olive']
l=[]
i=0
while(i<len(a)):
    l2=[]
    j=0
    while(j<len(a[i])):
        l2.append(a[i][j])
        j+=1
    l.append(l2)
    i+=1
print(l)