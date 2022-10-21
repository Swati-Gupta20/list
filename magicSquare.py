# l=[[8, 3, 4],
#    [1, 5, 9],
#    [6, 7, 2]]
# sum1=0
# sum2=0
# sum3=0
# sum4=0
# if len(l)!=len(l[0]):
#     print("it's not a magic square")
# i=0
# while(i<len(l)):  
#     j=0
#     col=0
#     while(j<len(l[i])):
#         col=col+l[j][i]
#         j+=1
#     k=0
#     row=0
#     while(k<len(l[i])):
#         row=row+l[i][k]
#         k+=1
#     a=0
#     d=0
#     p=0
#     while(a<len(l)):
#         d=d+l[a][p]
#         a+=1
#         p+=1
#     b=0
#     d2=0
#     p2=len(l)-1
#     while(b<len(l)):
#         d2=d2+l[b][p2]
#         b+=1
#         p2-=1
#     i+=1
#     sum1+=col
#     sum2+=row
#     sum3+=d
#     sum4+=d2
# if sum1==sum2 and sum2==sum3 and sum3==sum4 and sum4==sum1:
#     print("it's a magic square")
# else:
#     print("it's not a magic square")







# l=[[8, 3, 4],
#    [1, 5, 9],
#    [6, 7, 2]]
# sum1=0
# sum2=0
# sum3=0
# sum4=0
# if len(l)!=len(l[0]):
#     print("it's not a magic square")
# else:
#     i=0
#     while(i<len(l)):  
#         j=0
#         col=0
#         while(j<len(l[i])):
#             col=col+l[j][i]
#             j+=1
#         k=0
#         row=0
#         while(k<len(l[i])):
#             row=row+l[i][k]
#             k+=1
#         a=0
#         d=0
#         p=0
#         while(a<len(l)):
#             d=d+l[a][p]
#             a+=1
#             p+=1
#         b=0
#         d2=0
#         p2=len(l)-1
#         while(b<len(l)):
#             d2=d2+l[b][p2]
#             b+=1
#             p2-=1
#         i+=1
#         sum1+=col
#         sum2+=row
#         sum3+=d
#         sum4+=d2
#     if sum1==sum2 and sum2==sum3 and sum3==sum4 and sum4==sum1:
#         print("it's a magic square")
#     else:
#         print("it's not a magic square") 



l=[[8, 3, 4],
   [1, 5, 9],
   [6, 7, 2]]
# l=[[5, 3, 4],
#    [1, 5, 8],
#    [6, 7, 8]]
i=0
while(i<len(l)):
    fr=0
    fc=0
    sr=0
    sc=0
    tr=0
    tc=0
    dr=0
    dl=0
    j=0
    p=len(l)-1
    while(j<len(l)):
        fr+=l[0][j]
        fc+=l[j][0]
        sr+=l[1][j]
        sc+=l[j][1]
        tr+=l[2][j]
        tc+=l[j][2]
        dr+=l[j][j]
        dl+=l[j][p]
        j+=1
        p-=1
    i+=1
if fr==fc==sr==sc==tr==tc==dr==dl:
    print("it's a magic square")
else:
    print("it's not a magic square")


print("1st r",fr)
print(fc)
print("2nd r",sr)
print(sc)
print("3rd r",tr)
print(tc)
print("d r",dr)
print(dl)



    

l=[[5, 3, 4],
   [1, 5, 8],
   [6, 7, 8]]

