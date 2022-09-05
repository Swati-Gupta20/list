# l=[1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
# l2=[]
# x=20
# c=4
# i=c
# while(i<len(l)):
#     l.insert(i,x)
#     i+=c+1
# print(l)


# while(i<len(l)):
#     if c==4:
#         # l2.append(l[i])
#         l2.append(x)
#     else:
#         l2.append(l[i])
#     i+=1
#     c+=1
# print(l2)








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
