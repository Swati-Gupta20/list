# l=[4,6,4,3,3,4,3,4,3,8]
# k=3
# l2=[]
# for i in l:
#     f=l.count(i)
#     if f > k and i not in l2: 
#         l2.append(i)
# print(l2)

# or

l=[4,6,4,3,3,4,3,4,3,8]
k=3
l2=[]
i=0
while(i<len(l)):
    c=l.count(l[i])
    if c>k and l[i] not in l2:
        l2.append(l[i])
    i+=1
print(l2)