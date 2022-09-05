l=['.com', '.edu', '.tv']
string='https://www.w3resource.net'
# string='https://www.w3resource.com'

i=0
c=0
while(i<len(l)):
    if l[i] in string:
        c+=1        
    i+=1
if c==0:
    print("false")
else:
    print("true")
    
