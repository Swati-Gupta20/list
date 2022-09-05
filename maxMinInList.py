l=[36, 24, 13, 4, 5, 69, 7, 28, 9, 10]
l2=[]
max=0
min=1000
i=0
while(i<len(l)):
    if l[i]>max:
        max=l[i]
    elif l[i]<min:
        min=l[i]
    i+=1
print(max,"is maximum")
print(min,"is minimum")
