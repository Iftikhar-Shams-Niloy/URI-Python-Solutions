x = int(input())
y = int(input())
sum = 0

if x<y:
    i=x+1
    while i > x and i < y :
        if i%2 != 0 :
            sum = sum+i
            i = i+1
        else:
            i = i+1
elif y<x:
    i=y+1
    while i < x and i > y :
        if i%2 != 0 :
            sum = sum+i
            i = i+1
        else:
            i = i+1

print(sum)