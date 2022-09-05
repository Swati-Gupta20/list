# l=['Python', 'list', 'exercises', 'practice', 'solution']
# len=len(l)
# for i in range(len):
#     print(l[i][::-1])




'''reversed list'''

# l=['Python', 'list', 'exercises', 'practice', 'solution']
# len=len(l)
# l2=[]
# for i in range(len-1,-1,-1):
#     p=l[i][::-1]
#     l2.append(p)
# print(l2)



l=['Python', 'list', 'exercises', 'practice', 'solution']
l2=[]
i=0
while(i<len(l)-1):
    a=l[i],l[i+1]
    l2.append(list(a))
    i+=2
print(l2)
# j=0
# while(j<len(l2)):
#     print(l2[-j+1])
#     j+=1