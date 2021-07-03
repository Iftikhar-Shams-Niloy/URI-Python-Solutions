N = int(input())

for i in range(N):
    X, Y = list(map(int, input().split(" ")))
    res = 0
    if X > Y:
        big = X
        small = Y + 1
    else:
        big = Y
        small = X + 1
    for j in  range(small,big):

        if small % 2 != 0:
            res = res + small
            small = small + 1
        else:
            small = small + 1

    print(res)
