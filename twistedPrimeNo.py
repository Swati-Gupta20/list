num1=int(input('enter no:-'))
num2=int(input('enter no:-'))
l=[]
dif=num2-num1
k=0
while k<=dif:
    l.append(num1)
    num1+=1
    k+=1
lp=[]
i=0
while i<len(l):
    j=2
    c=0
    while j<l[i]:
        if l[i]%j==0:
            c+=1
        j+=1
    if c==0:
       lp.append(l[i])
    i+=1  
print('prime numbers'+':',lp)
a=0
l3=[]
while a<len(lp):
    b=2
    count=0
    num=str(lp[a])
    re=num[::-1]
    while(b<int(re)):
        if int(re)%b==0:
            count+=1
        b+=1
    if count==0:
        l3.append(int(re))
    a+=1
print('twisted prime numbers'+':',l3)




