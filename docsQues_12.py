num=input("enter no.:-")
len=len(num)
num1=int(num)
l=[]
i=0
place=1
while(i<len):
    num2=num1%10
    expand=num2*place
    num1=num1//10
    place*=10
    l.append(str(expand))
    i+=1
l.reverse()
p="+".join(l)
print(p)