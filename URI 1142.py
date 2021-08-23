N = int(input())
X = 1
z = N*4
for i in range(N):
    while X <= z:
        if X%4 != 0:
            print("%d"%X, end=" ")
            X += 1
        else:
            print("PUM")
            X += 1
    N += 1
