flag = 0
while flag == 0:
    H1,M1,H2,M2 = list(map(int,input().split(" ")))
    if H1 < H2 :
        hours = H2 - H1
        if M1 <= M2 :
            minutes = M2 - M1
            total = (hours * 60) + minutes
        else:
            minutes =(M1 - M2)
            total = (hours * 60) - minutes
    elif H1 > H2 :
        if M1 > M2:
            hours = 24 - ((H1 - H2)+1)
            minutes = 60 - (M1 - M2)
            total = (hours * 60) + minutes
        else :
            hours = 24 - (H1 - H2)
            minutes =  (M2 - M1)
            total = (hours * 60) + minutes

    elif H1 == H2 :
        if M1 > M2:
            hours = 23
            minutes = 60 - (M1 - M2)
            total = (hours * 60) + minutes
        else :
            hours = 0
            minutes =  (M2 - M1)
            total = (hours * 60) + minutes


    if H1==M1==H2==M2==0:
        flag = 1
        break

    print(total)