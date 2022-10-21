l=[57,57,-57,57]
max=-1000
smax=-1000
i=0
while i<len(l):
    if l[i]>max:
        max=l[i]
    i+=1
j=0
while j<len(l):
    if l[j]>smax and l[j]!=max:
        smax=l[j]
    j+=1
# print(smax)


