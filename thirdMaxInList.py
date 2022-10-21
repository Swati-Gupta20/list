l=[57,29,567,23,66,99]
max=-1000
smax=-1000
tmax=-1000
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
k=0
while k<len(l):
    if l[k]>tmax and l[k]!=max and l[k]!=smax:
        tmax=l[k]
    k+=1
print(tmax)