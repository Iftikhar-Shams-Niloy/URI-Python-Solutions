flag = 0
while flag ==0 :
    X,Y = list(map(int, input().split(" ")))
    if X == 0 or Y == 0:
        flag = 1
        break
    elif X>0 and Y>0 :
        print("primeiro")
    elif X>0 and Y<0:
        print("quarto")
    elif X<0 and Y<0:
        print("terceiro")
    elif X<0 and Y>0:
        print("segundo")
