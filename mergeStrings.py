l=['a','b','a','a','a','c','d','c','b','c','c','g']
i=0
s=''
while i<len(l)-1:   
    if l[i]==l[i+1]:
        s+=''
    elif l[i]!=l[i+1]:
        s+=l[i] 
    i+=1
s+=l[-1]
print(s)



# l=['a','b','a','a','c','d','c','b','c']
# i=0
# s=''
# while i<len(l):   
#     if l[i]!=l[i-1]:
#         s+=l[i] 
#     i+=1
# print(s)