l=['a','b','c','a','b','b','d','d','d','d','c','a']
l2=[]
count=0
i=0
while(i<len(l)):
      count=l.count(l[i])
      a=l[i],count
      if list(a) not in l2:
        l2.append(list(a))
      i+=1
print(l2)
