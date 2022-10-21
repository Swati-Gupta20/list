
# names_list = ["annu", "shivam", "deepa", "pooja", "rupa", "dhruv", "alok"]
# # print("shivam" in names_list)
# print(names_list.count(4))
# names_list.remove("deepa")
# print(names_list)


# l=[1, 1, 2, 3, 4, 4, 5, 1]
# # o/p=[[2, 1], 2, 3, [2, 4], 5, 1]
# l2=[]
# i=0
# while i<len(l):
#     print(l[i],end=" ")
#     i+=1

# a=438+500+60+50+390
# print(a)


# a='swati'
# i=0
# while i<3:
#     print(a,end="")
#     i+=1


# def run_length_encoding(seq):

#   compressed = []
#   count = 1
#   char = seq[0]
#   for i in range(1,len(seq)):
#     if seq[i] == char:
#       count = count + 1
#     else :
#       compressed.append([char,count])
#       char = seq[i]
#       count = 1
#   compressed.append([char,count])
#   return compressed
# print(run_length_encoding("aabcddddadnss"))



# l=[1, 1, 2, 3, 4, 4, 5, 1]
# l2=[]
# count=0
# i=0
# while(i<len(l)):
#     if l[i] in l:
#         # count+=1
#         if l[i]==l[i-1]:
#             count+=1
#             l2.append([count,l[i]])
#         else:
#             l2.append(l[i])
#     i+=1
# print(l2)
    
# l=[1, 1, 2, 3, 4, 4, 5, 1]
# l2=[]
# i=0
# while(i<len(l)):
#     c=1
#     while i+1<len(l): #and l[i]==l[i+1]:
#         if l[i]==l[i+1]:
#            c+=1
#            l2.append([c,l[i]])
#         elif l[i]!= l[i+1]:
#             l2.append(l[i])
#         i+=1
#     i+=1
# p="".join(str(l2))
# print(p)


# l=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# len=len(l)
# i=0
# maxl=0
# minl=0
# while(i<len):
#     j=0
#     # c=1
#     while(j<len):
#         if int(len(l[i]))>maxl:
#             maxl+=len[i]
#         elif len(l[i])<maxl and len(l[i])>minl:
#             minl+=len(l[i])
#         j+=1
#     i+=1
# print(len(maxl),maxl)
# print(len(minl),minl)






# # a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# a=[2,4,6,8,10]
# len=len(a)
# l=[]
# i=0
# while(i<len):
#     b=a[i]
#     c=b
#     d=b-c
#     i+=1
#     l.append(d)
# print(l)


# list = [1,2,3,1,2,2]
# l=[]
# i=0
# while(i<len(list)):
#     if list[i] not in l:
#         l.append(list[i])
#     i+=1
# print(l)


# l=[4,6,4,3,3,4,3,4,3,8]
# # k = 3
# l2=[]
# i=0
# while(i<len(l)):
#     if l[i] not in l:
#        l2.append(l[i])
#     i+=1
# print(l2)

# l=[4,6,4,3,3,4,3,4,3,8]
# l2=[]
# i=0
# while(i<len(l)):
#     if l[i] not in l2:
#         l2.append(l[i])
#         a=l2.count(l[i])
#     i+=1
# print(l2)

# print(a)

# l=[4,6,4,3,3,4,3,4,3,8]
# k=3
# l2=[]
# for i in l:
#     f=l.count(i)
#     if f > k and i not in l2: 
#         l2.append(i)
# print(l2)


# i=100
# while i<300:
#     print(i-99)
#     i+=1

# l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# l=[2,4,5,8,10,12,14]
# a=1
# l2=[]
# i=0
# while(i<len(l)):
#     k=l[i]-a+1
#     l2.append(k)
#     a+=1
#     i+=1

# print(l2)

# l=['Python', 'list', 'exercises', 'practice', 'solution']
# len=len(l)
# for i in range(len):
#     print(l[i][::-1])




'''Write a Python program to find the list with maximum and minimum length.
Original list:
[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
List with maximum length of lists:
(3, [13, 15, 17])
List with minimum length of lists:
(1, [0])'''

# l=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# size=len(l)
# max=0
# min=1000
# i=0
# while(i<size):
#     j=0
#     while(j<size):
#         if len(l[i])>max:
#             max=len(l[i])
#         elif len(l[i])<min:
#             min=len(l[i])
#         j+=1
#     i+=1
# print(max,l[i-1])
# print(min,l[i-1])


# l=[[7,1], [8, 3], [5, 7], [9, 11], [13, 15, 17]]
# l2=[]
# i=0
# while(i<len(l)):
#     j=0
#     sum=0
#     size2=len(l[i])
#     while(j<size2):
#         sum=l[i][j]
#         l2.append(sum)

#         j+=1
#     i+=1
# print(l2)


    

# l=[36, 24, 13, 4, 5, 69, 7, 28, 9, 10]
# l2=[]
# max=0
# min=1000
# i=0
# while(i<len(l)):
#     if l[i]>max:
#         max=l[i]
#     elif l[i]<min:
#         min=l[i]
#     i+=1
# print(max,"is maximum")
# print(min,"is minimum")


# password=input("enter password:-")
# if (password<='z'and'Z')and (password>="a"and'A')and (password<='9' and password>='1' and "@"or"#"or'$'or'%') in password:
#     print("strong password") 
# if password<='z' and password<='Z' and password>="a" and password>='A' not in password:
#     print("Use upper case")
# if "@"or"#"or'$'or'%' not in password:
#     print("use special character")
# if password<='9' and password>='1'not in password:
#     print("use numbers")
# else:
#     print("weak password")



# password=input("enter password:-")
# if len(password)<6:
#     print("length should not be less than 6")


# rle 




# password=input("enter the password")
# if len(password)>6 or len(password)<9:
#     if "@"in password or "$"in password or "#"in password:
#         if "a" in password or "b" in password or "c" in password or "d" in password or "e" in password or "f" in password or "g" in password or "h" in password or "i" in password or "j" in password or "k" in password or "l" in password or "m" in password or "n" in password or "o" in password or "p" in password or "q" in password or "r" in password or "s" in password or "t" in password or "u" in password or "v" in password or "w" in password or "x" in password or "y" in password or "z" in password:
#             if "A" in password or "B" in password or "C" in password or "D" in password or "E" in password or "F" in password or "G" in password or "H" in password or "I" in password or "J" in password or "K" in password or "L" in password or "M" in password or "N" in password or "O" in password or "P" in password or "Q" in password or "R" in password or "S" in password or "T" in password or "U" in password or "v" in password or "W" in password or "X" in password or "Y" in password or "Z" in password:
#                 if "1" in password or "2" in password or "3" in password or"4" in password or "5" in password or "6" in password or "7" in password or "8" in password or "9" in password:
#                     print("strong password")
#                 else:
#                     print("enter the digit")
#             else:
#                 print("enter the upper character")
#         else:
#             print("enter the lower character")
#     else:
#         print("enter the special character")
# else:
#     print("weak password")





# print(l2[:3])

# l=[[0, 1, 2],
#    [2, 3, 4],
#    [3, 4, 5, 6],
#    [7, 8, 9, 10, 11],
#    [12,13,14]]
# i=0
# while(i<len(l)):
#     j=0
#     sum=0
#     while(j<len(l)):
#         sum=sum+l[j][i]
#         print(l[j][i],end=" ")
#         j+=1
#     i+=1
#     print()


# print(29/5)

# l=[1,1,1,3,4,4,5,1]
# l2=[]
# i=0
# while(i<len(l)-2):
#     j=0
#     c=1
#     while(j<i+1):
#         if l[i]==l[i+1] and l[i+1]==[l[i+2]]:
#             c+=1
#         a=c,l[i+2]
#         l2.append(list(a))
#         j+=1
#     i+=2
# print(l2)

# l=[1,1,1,3,4,4,5,1]
# l2=[]
# for i in range(len(l)-2):
#     if l[i]==l[i+1] and l[i+1]==[l[i+2]]:
#         l2.append(l[i])
#     elif l[i]==l[i+1] or l[i+1]==[l[i+2]]:
#         l2.append(l[i+1])
#     # elif l[i]!=l[i+1]:
#     #     l2.append(l[i+1])
# print(l2)





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


# l=[1, 1, 2, 3, 4, 4, 5, 1]

# l2=''
# l3=[]
# i=0
# while(i<len(l)):
#     count=1
#     if i+1<len(l) and l[i]==l[i+1]:
#         count+=1
#         i+=1
    
#     elif i+1<len(l) and l[i]!=l[i+1]:
#         l2=l2+str(l[i])
#     i+=1
# print(l2)

# u_name=input("enter the user_name :  ")
# password=input("enter the password :  ")
# p=len(password)
# numbers = "0123456789"
# lower_case = "abcdefghijklmnopqrstuvwxyz"
# upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# special_chr = "!@#$%^&*()-+"
# n,l,u,s=0,0,0,0
# i=0
#         while i<len(password):
        #     if password[i] in numbers:
        #         n=n+1
        #     if password[i] in lower_case:
        #         l=l+1
        #     if password[i] in upper_case:
        #         u=u+1
        #     if password[i] in special_chr:
        #         s=s+1
        #     i=i+1
        # if p>=6:
        #     if n>=1 and l>=1 and u>=1 and s>=1 :
        #         print("strong password")
        #     else:
        #         print("invilade")
        # else:
        #     print("no")
    


# a="Man"
# l=[]
# i=0
# while i<len(a):
#         l.append(a[i])
#         i+=1
# print(l)



# a=[1,2,1,3,4,2,3,4,7]
# l=[]
# i=0
# c=0
# while(i<len(a)):
#         c=a.count(a[i])
#         if c==1:
#           l.append(a[i])
#         i+=1
# print(l)



# a=[[1,2,3],[4,5,6],[7,8]]
# l=[]
# sum=0
# i=0
# while(i<len(a)):
#         sum=0
#         j=0
#         while(j<len(a[i])):
#                 sum+=a[i][j]
#                 j+=1
#         l.append(sum)
#         i+=1
# l.append(sum)
# print(l)


# a=[1,2,3,4,5,6,]
# l=[]
# i=0
# while(i<len(a)):
#         if a[i] not in l:
#                 b=(i+1)*(-1)
#                 l.append(a[b])
#                 l.append(a[i])
#         i+=1
# print(l)


# a=[[1,0,1],[0,-2,3]]
# i=0
# max=0
# while(i<len(a)):
#         j=0
#         sum=0
#         while(j<len(a[i])):
#                 sum+=a[i][j]
#                 j+=1
#         i+=1
#         if sum>max:
#                 max=sum
# print(max)  

# a=[4,9,5]
# b=[9,4,9,8,4]
# l=[]
# c=a,b
# i=0
# j=0
# while(i<len(list(c))):
#         d=list(c)
#         l.append(d[i][j])
#         i+=1
# l.reverse()
# print(l)


# a="hello"
# l=''
# i=0
# while(i<len(a)):
#         if a[i]=='e':
#            l+='o'
#         elif a[i]=='o':
#            l+='e'
#         else:
#            l+=a[i]
#         i+=1
# print(l)





# a=int(input("enter 1st no.:-"))
# b=int(input("enter 2nd no.:-"))
# c=int(input("enter 3rd no.:-"))
# d=int(input("enter 4th no.:-"))
# l=[a,b,c,d]
# i=0
# count=0
# while(i<len(l)-1):
#         if l[i+1]==l[i]+1:
#              count+=1
#         i+=1
# if count==len(l)-1:
#         print("yes")
# else:
#         print("no")


# a=[[1,2,3],[4,5,6],[7,8,9]]
# l=[]
# sum=0
# i=0
# while(i<len(a)):
#         j=0
#         while j<len(a[i]):
#             sum=sum+a[j][i]
#             j+=1
#         i+=1
#         l.append(sum)
# print(l)


# l=['abc', 'xyz', 'aba', '1221']



# l=[36, 24, 13, 4, 5, 69, 7, 28, 9, 10]
# l2=[]
# max=0
# min=1000
# i=0
# while(i<len(l)):
#     if l[i]>max:
#         max=l[i]
#     elif l[i]<min:
#         min=l[i]
#     i+=1
# print(max,"is maximum")
# print(min,"is minimum")

# l=[36, 24, 13, 4, 5, 69, 7, 28, 9, 10]
# l2=[]
# max=0
# smax=0
# min=1000
# i=0
# while(i<len(l)):
#     if l[i]>max:
#         max=l[i]
#     elif l[i]<min:
#         min=l[i]
#     elif l[i]>smax and l[i]!=min and l[i]!=max:
#         smax=l[i]
#     i+=1
# print(max,"is maximum")
# print(min,"is minimum")
# print(smax)



l=[1,2,3,4,5,6,7,8]
a=int((len(l)-1)/2)
print(l[a])    

