import math

R1 = input().split(" ")
R2 = input().split(" ")

x1, y1 = R1
x2, y2 = R2

dis = math.sqrt((float(x2) - float(x1))**2 +(float(y2)-float(y1))**2)
print("%.4lf" %dis)