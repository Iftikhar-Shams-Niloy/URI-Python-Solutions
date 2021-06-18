x,y,z = list(map(float,input().split(" ")))
flag1 = 0
flag2 = 0
if x>y and x>z :
    a = x
    b = y
    c = z
elif y>x and y>z:
    a = y
    b = x
    c = z
else:
    a = z
    b = x
    c = y

if a >= b+c:
    print("NAO FORMA TRIANGULO")
    flag1 =1
if (a*a) == ((b*b) + (c*c)) and flag1 == 0:
    print("TRIANGULO RETANGULO")
if (a*a) > (b*b + c*c) and flag1 == 0:
    print("TRIANGULO OBTUSANGULO")
if (a*a) < (b*b + c*c) and flag1 == 0 :
    print("TRIANGULO ACUTANGULO")
if a==b and b==c and flag1 == 0 :
    print("TRIANGULO EQUILATERO")
    flag2 = 1
if flag1==0 and flag2 == 0 :
    if x==y or x==z:
        print("TRIANGULO ISOSCELES")