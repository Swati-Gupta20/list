# l=[[0, 1, 2], 
#    [2, 3, 4], 
#    [3, 4, 5, 6], 
#    [7, 8, 9, 10,11], 
#    [12,13,14]]
# l2=[]
# i=0
# while(i<len(l)):
#     j=0
#     sum=0
#     while(j<len(l[i])):
#         sum=sum+l[i][j]
#         j+=1
#     ave=sum/len(l[i])
#     l2.append(ave)
#     i+=1
# print(l2)





l=[[0, 1, 2,'',''], 
   [2, 3, 4,'',''], 
   [3, 4, 5, 6,''], 
   [7, 8, 9, 10,11], 
   [12,13,14,'','']]
l2=[]
i=0
while(i<len(l)):
    j=0
    sum=0
    c=0
    while(j<len(l)):
        if type(l[j][i])==int:
            sum=sum+l[j][i]
        if l[j][i]!='':
            c+=1        
        j+=1
    ave=sum/c
    l2.append(ave)
    i+=1
print(l2)