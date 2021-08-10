X = int(input())
Y = int(input())

if X<Y :
    Z = X+1
    for i in range (Z, Y):
        if Z%5 == 2 or Z%5 == 3:
            print(Z)
        Z += 1
else:
    Z = Y+1
    for i in range (Z, X):
        if Z%5 == 2 or Z%5 == 3:
            print(Z)
        Z += 1