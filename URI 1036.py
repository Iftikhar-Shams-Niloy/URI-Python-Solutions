import math
A, B, C = list(map(float,input().split(" ")))
if A!=0 and (B*B -4*A*C)>=0:

    delta =(B)**2 - 4*((A)*(C))
    R1 = (-1*(B) + math.sqrt(delta)) / (2*(A))
    R2 = (-1*(B) - math.sqrt(delta)) / (2*(A))
    print("R1 = %.5f" %R1)
    print("R2 = %.5f" %R2)

else:
    print("Impossivel calcular")