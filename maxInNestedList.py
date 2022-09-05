l=[[7,1], [8, 3], [5, 7], [9, 11], [13, 15, 17]]
size=len(l)
l2=[]
i=0
while(i<size):
    j=0
    max=0
    size2=len(l[i])
    while(j<size2):
        if l[i][j]>max:
            max=l[i][j]
        j+=1
    i+=1
    l2.append(max)
print(l2)
max=0
i=0
while(i<len(l2)):
    if l2[i]>max:
        max=l2[i]
    i+=1
print("maximum in l2 is",max)