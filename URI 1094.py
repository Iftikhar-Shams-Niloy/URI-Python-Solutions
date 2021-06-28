N = int(input())
total_rabbit = 0
total_rat = 0
total_frog = 0
total = 0

for i in range(N):
    A,B = list(map(str,input().split(" ")))
    A = int(A)
    if B == "C":
        total_rabbit = total_rabbit + A
    elif B == "R":
        total_rat = total_rat + A
    elif B == "S":
        total_frog = total_frog + A
    total = total+A
per_rabbit = (total_rabbit/total)*100
per_rat = (total_rat/total)*100
per_frog = (total_frog/total)*100
print("Total : %d cobaias" %total)
print("Total de coelhos: %d" %total_rabbit)
print("Total de ratos: %d"%total_rat)
print("Total de sapos: %d"%total_frog)
print("Percentual de coelhos: %.2f %%" %per_rabbit)
print("Percentual de ratos: %.2f %%" %per_rat)
print("Percentual de sapos: %.2f %%" %per_frog)

