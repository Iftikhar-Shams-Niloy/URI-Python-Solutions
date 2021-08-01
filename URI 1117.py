flag = 0
total = 0
while flag < 2:
    N = float(input())
    if N>= 0 and N<=10 :
        total = total + N
        flag += 1
    else:
        print("nota invalida")
avg = total/2
print("media = %.2f"%avg)

