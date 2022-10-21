l=input('enter string:-')
s=''
p=''
i=0
while i<len(l):
    if l[i].isalpha():
        p+=(l[i].lower())
    if l[(i+1)*-1].isalpha():        
        a=l[(i+1)*-1].lower()
        s+=a
    i+=1
if s==p:
    print(l,"\npalindrome")
else:
    print(l,"\nnot palindrome")
