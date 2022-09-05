# l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# l=[2, 4, 6, 8,12,15]

# size=len(l)
# l2=[]
# for i in range(size-1):
#     d=l[i+1]-l[i]
#     l2.append(d)
# print(l2)


# while loops:-

l=[2,4,6,8,12,15]
l2=[]
i=0
while i<len(l)-1:
    d=l[i+1]-l[i]
    l2.append(d)
    i+=1
print(l2)