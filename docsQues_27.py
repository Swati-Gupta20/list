# l=[1, 2, 3]
# for i in range(3):
#     for j in range(3):
#         for k in range(3):
#             if i!=j and j!=k and k!=i:
#                 print(l[i],l[j],l[k])

# or


l=[1, 2, 3]
i=0
while(i<len(l)):
    j=0
    while(j<len(l)):
        k=0
        while(k<len(l)):
            if i!=j and j!=k and k!=i:
                print(l[i],l[j],l[k])
            k+=1
        j+=1
    i+=1