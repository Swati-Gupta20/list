# in list:-

# l="WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
# # l="aabcddddadnss"
# l2=[]
# i=0
# while(i<len(l)):
#     count=1
#     if l[i]==l[i+1]:
#         while i+1<len(l) and l[i]==l[i+1]:
#             count+=1
#             i+=1
#         a=count,l[i]
#         l2.append(list(a))
#     else:
#         l2.append(l[i])            
#     i+=1
# print(l2)


# in string:-

# l="aabcddddadnss"
# l2=''
# l3=[]
# i=0
# while(i<len(l)):
#     count=1
#     while i+1<len(l) and l[i]==l[i+1]:
#         count+=1
#         i+=1
#     a=str(count)+str(l[i])
#     l2=l2+a
#     i+=1
# print(l2)

l="aabcddddadnss"
l="WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
l2=[]
i=0
while(i<len(l)):
    count=1
    while i+1<len(l) and l[i]==l[i+1]:
        count+=1
        i+=1
    a=count,l[i]
    l2.append(list(a))                 
    i+=1
print(l2)




