i = 0
flag = 0
total = 0
while i < 6:
    num = float(input())
    if num > 0 :
        flag = flag+1
        total= total+num
        i=i+1
    else:
        i=i+1
        continue
avg = total/flag
print("%f valores positivos\n%f"%(flag,avg))
