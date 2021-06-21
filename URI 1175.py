x = []
for i in range(20):
    num = int(input())
    x.append(num)
x.reverse()
for j in range(20):
    print("N[%d] = %d"%(j,x[j]))