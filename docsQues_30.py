l = [2, -7, 5, -64, -14]
n=0
p=0
i=0
while(i<len(l)):
    if l[i]<0:
        n=n+1
    elif l[i]>0:
        p+=1
    i+=1
print("neg=",n,"pos=",p)