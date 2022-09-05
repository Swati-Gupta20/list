binary_number = [1, 0, 0, 1, 1, 0, 1, 1]
len=len(binary_number)
dec=0
for i in range(len):
    power=len-(i+1)
    dec=dec+binary_number[i]*2**power
print(dec,"is the decimal no. of",binary_number)