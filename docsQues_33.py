# l= [12, 67, 98, 34]
l=[15, 81, 11, 234]
l2=[]
i=0
while(i<len(l)):
    s=0
    j=0
    num=l[i]
    while(j<len(str(l[i]))):
        n=num%10
        s=s+n   
        j+=1
        num//=10
    l2.append(s)
    i+=1

print(l2)



l=['12','34','44','62']
l2=[]
i=0
while(i<len(l)):
    j=0
    sum=0
    while(j<len(l[i])):
        sum+=int(l[i][j])
        j+=1
    l2.append(sum)
    i+=1
print(l2)