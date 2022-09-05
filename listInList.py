
# o/p-[[1,"red"],[2,"green"],[3,"black"],[4,"white"],[5,"black"]]
l=[1,"red",2,"green",3,"black",4,"white",5,"black"]
l2=[]
i=0
while(i<len(l)-1):
    a=l[i],l[i+1]
    l2.append(list(a))
    i+=2
print(l2)

# reversed output
j=1
e=[]
while(j<len(l2)+1):
    e.append(l2[-j])
    j+=1
print(e)
# or
print(l2[::-1])








# l=[[1,"red"],[2,"green"],[3,"black"],[4,"white"],[5,"black"]]
# # o/p-[1,"red",2,"green",3,"black",4,"white",5,"black"]
# l2=[]
# i=0
# while(i<len(l)):
#     j=0
#     while(j<len(l[i])):
#         a=l[i][j]
#         l2.append(a)
#         j+=1
#     i+=1
# print(l2)