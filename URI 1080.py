x = 0
pos = 0
i=0
while i < 100:
    N = int(input())
    if N>x :
        x = N
        pos = i
    i = i+1

print(x)
print(pos+1)