a=[12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
l=[]
i=0
n=3
while(i<len(a)):
    l2=[]
    j=0
    while(j<n):
        if i==len(a) and j==n-1:
            break
        l2.append(a[i])
        i+=1
        j+=1
    l.append(l2)
    i+=1-1
print(l)




# a=[12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
# l=[]
# i=0
# n=6
# while(i<len(a)):
#     l2=[]
#     j=0
#     while(j<n):
#         if i==len(a):
#             if i==15 and j==n-(len(l[-2])-len(l[-1])):
#                 break
#         l2.append(a[i])
#         i+=1
#         j+=1
#     l.append(l2)
#     i+=1-1
# print(l)