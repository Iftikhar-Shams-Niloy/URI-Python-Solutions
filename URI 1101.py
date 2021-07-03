flag = 0
while flag == 0 :
    M, N = list(map(int, input().split(" ")))
    total = 0
    if M <= 0 or N <= 0:
        flag =1
        break
    elif M > N:
        big = M
        small = N
    elif M < N:
        big = N
        small = M

    for i in range(small,(big+1)):
        print("%d"%small, end=" ")
        total = total + small
        small += 1
    print("Sum=%d" %total)
