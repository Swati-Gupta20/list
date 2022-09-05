number=30
n = [10, 11, 12, 13, 14, 17, 18, 19]
l2=[]
i=0
while(i<len(n)-1):
    j=0
    k=0
    while(j<len(n)):
        if (n[i]+n[j]==number) and n[i]<n[j]:
            k=n[i],n[j]
            # print(k)
            l2.append(list(k))
        j+=1   
    i+=1
print(l2)