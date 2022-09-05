# l=[1234, 122, 1984, 19372, 100]
l=[1234, 922, 1984, 19372, 100]
# l=['aabc', 'abc', 'ab', 'a']

len=len(l)
count=1
i=0
while(i<len-1):
    j=0
    while(j<1):
        if str(l[i])[j]==str(l[i+1])[j]:
            count+=1
        j+=1
    i+=1
if count==len:
    print("true")
else:
    print("false")


