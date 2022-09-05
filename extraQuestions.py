# Q-1:

# l=[1,7,9,12,22]
# l=[12,18,23,32]

# l2=[]
# i=l[0]
# while i<l[-1]+1:
#     if l not in l2:
#         l2.append(i)
#     i+=1
# print(l2)


# Q-2:

# names=["swati","ariya","seminao","vilichon","jian","teresa"]
# rooms=[1,2,3]
# i=0
# while i<len(rooms):
#     j=0   
#     while j<len(rooms):
#         print("Room:",rooms[j])
#         print("1.",names[i])
#         print("2.",names[i+1]) 
#         i+=2        
#         j+=1           
    


#  Q-3.

# l=[0,7,[1,3,8],[6,9,10,[4,5]]]
# # o/p:1,6,4,0
# # a=l[2][0],l[3][0],l[3][3][0],l[0]
# a=l[2][0]
# b=l[3][0]
# c=l[3][3][0]
# d=l[0]
# print(a,',',b,',',c,',',d)


# Q-4.

# user=list(input("enter letters:-"))
# user2=int(input("enter any no."))
# print(user[user2])

# Q-5.

# a=78954
# l=[]
# i=0
# while i<len(str(a)):
#     b=str(a)
#     l.append(int(b[i]))
#     i+=1
# print(l)


# Q-6.

# l=["swati","gupta"]
# l2=[]
# i=0
# while i<len(l):
#     a=l[i][0].upper()
#     l2.append(a)
#     i+=1
# b=".".join(l2)
# print(b)



# l=[1,7,5,34,67,3,23,45,9]
# i=0
# while(i<len(l)):
    # j=0
    # c=0
    # while(j<len(l)):
    #     if l[j]>l[i]:
    #         c+=1

# l=[1,7,5,34,67,3,23,45,9]
# l2=[]
# i=0
# while(i<len(l)):
#     j=0
#     c=0
#     while(j<len(l)):
#         if l[i]<l[j]:
#             c+=1
#         j+=1
#     i+=1
#     l2.append(c)
# print(l2)




# l="swati is singing very loudly"
# print(l[0])
# a=l.count(" ")
# a=len(l)
# print(a)
# l="swati is singing very loudly"
# i=0
# s=''
# while(i<len(l)):
#     s=s+l[i]
    # if i==7:
    #     continue
    # elif i==8:
    #     s=s+l[i]+"was"
#     i+=1
# print(s)

# print(len(s))
# if 'is' in l:
#     print("true")
# else:
#     print('false')




# l="swati is singing very loudly"
# s=l.replace("is","was")
# s=l.replace("singing","")
# print(s)




# n1=int(input("enter no.:-"))
# n2=int(input("enter no. of times:-"))
# i=0
# p=1
# while(i<n2):
#     n=n1*p
#     p*=10
#     i+=1
#     print(n)



# l=[2,5,20,32,6,19,54,12,15,30]
# l.sort()
# max=[]
# min=[]
# sum1=0
# sum2=0
# i=0
# while(i<len(l)):
#     if l[0]<l[i]:
#         sum1+=l[i]
#         max.append(l[i])
#     if l[-1]>l[i]:
#         sum2+=l[i]
#         min.append(l[i])
#     i+=1
# print(max,sum1)
# print(min,sum2)



# l=input("enter no.")
# l2=[]
# i=0
# while(i<len(l)):
#     l2.append(l[i])
#     i+=1
# print(l2)



# l=["swati",1,2,3,"archana",4,5]
# l1=[]
# l2=[]
# l3=[]
# i=0
# while(i<len(l)):
#     if type(l[i])==int and l[i]<=3:
#         l1.append(l[i])
#     elif type(l[i])==int and l[i]>3:
#         l2.append(l[i])
#     else:
#         l3.append(l[i])
#     i+=1
# print(l1)
# print(l2)
# print(l3)


a=[1,2,3,4,5,6]
# o/p:[1,3,5,10]
l=[]
i=0
while(i<len(a)):
    sum=0
    j=0
    while(j<=i):
        sum+=a[j]
        j+=1
    i+=1
    l.append(sum)
print(l)