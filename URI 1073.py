N = int(input())
i = 1
while i <= N :
    if i%2 == 0 :
        square = i**2
        print("%d^2 = %d"%(i,square))
        i = i+1
    else:
        i = i+1