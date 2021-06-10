A,B,C = list(map(float,input().split(" ")))

if A<(B+C) and B<(A+C) and C<(A+B):
    peri_tri = A + B + C
    print("Perimetro = %.1f" %peri_tri)
else:
    area_trap = ((A+B)*C)/2
    print("Area = %.1f" %area_trap)