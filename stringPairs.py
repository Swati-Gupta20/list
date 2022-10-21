a=input('enter string:-')
n=int(input('enter times:-'))
i=0
while i<len(a)-1:
    s=''
    j=0
    while j<n:
        if i==len(a)-1:
            m=len(a)%n
            n=m 
        s+=a[i]
        i+=1
        j+=1
    i+=1-1
    print(s)


# a=input('enter string:-')
# n=int(input('enter times:-'))
# i=0
# while i<len(a):
#     print(a[i:i+n])
#     i+=n
