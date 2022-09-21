t = [6, 8, 4, 3, 9, 56, 0, 34, 7, 15]
i=0
while i<len(t)-1:
    j=0
    while j<len(t)-1:
        if t[j]>t[j+1]:
            t[j],t[j+1]=t[j+1],t[j]
        j+=1
    i+=1

print(t)