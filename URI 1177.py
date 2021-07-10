n1 = int(input())
n2 = 0
for i in range(1000):
    print("N[%d] = %d"%(i, n2))
    n2 += 1
    if n2 == n1 :
        n2 = 0
