a=['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']
l='f'
c=a.count(l)
i=0
while(i<len(a)):
    if a[i]==l:
        c-=1
    if c==0:
        print(i)
        break
    i+=1
