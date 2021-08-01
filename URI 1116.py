N = int(input())
i = 0
while i < N :
    X,Y = list(map(int,input().split(" ")))
    if Y == 0:
        print("divisao impossivel")
    else:
        result = X/Y
        print(result)
    i += 1