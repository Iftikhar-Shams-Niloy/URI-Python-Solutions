N = int(input())
X = 1
for i in range(N):
    Y = 1
    while Y <= 4:
        if Y <= 3:
            Z = X ** Y
            print("%d" % Z, end=" ")
            Y += 1
        elif Y == 4:
            print("")
            Y += 1
    X += 1

