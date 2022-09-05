l="swati"
l2=''
c=0
i=0
while(i<len(l)):
     j=0
     while(j<=i):        
        c=l.count(l[i]) 
        if l[i] not in l2:
            l2+=str(c)+l[i]
        j+=1        
     i+=1
print(l2)