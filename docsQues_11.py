# n=9119
# n2=int(n)
# i=0
# while(i<len(str(n))):
#     num=n2%10
#     square=num**2
#     n2=n2//10
#     print(square,end="")
#     i+=1





n=input("enter no:-")
i=0
while(i<len(n)):
    print(int(n[i])**2,end="")
    i+=1


