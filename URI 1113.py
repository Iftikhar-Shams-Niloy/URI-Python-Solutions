flag = 0
while flag == 0:
    X,Y = list(map(int,input().split(" ")))
    if X == Y :
        flag = 1
        break
    elif X > Y :
        print("Decrescente")
    elif X < Y:
        print("Crescente")