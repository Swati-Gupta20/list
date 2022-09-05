n=int(input("start value:-"))
n2=int(input("end value:-"))
l=[]
for i in range(n,n2):
    if i<0:
        l.append(str(i))
p=','.join(l)
print(p)