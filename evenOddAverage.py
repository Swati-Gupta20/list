l=[23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
sumeven=0
sumodd=0
c1=0
c2=0
i=0
while(i<len(l)):
    if l[i]%2==0:
        c1+=1
        sumeven+=l[i]
    else:
        c2+=1
        sumodd+=l[i]
    i+=1
ave1=sumeven/c1
ave2=sumodd/c2
print(ave1)
print(ave2)