num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())
num5 = float(input())
num6 = float(input())
flag = 0
total=0
if num1 > 0 :
    flag = flag+1
    total = total+ num1
if num2 > 0 :
    flag = flag+1
    total = total + num2
if num3 > 0:
    flag = flag + 1
    total = total + num3
if num4 > 0 :
    flag = flag+1
    total = total + num4
if num5 > 0 :
    flag = flag+1
    total = total + num5
if num6 > 0 :
    flag = flag+1
    total = total + num6

avg = total/flag
print("%d valores positivos"%flag)
print(avg)