value = input().split(" ")

A, B, C = value

AB = (int(A) + int(B) + abs(int(A) - int(B)))  / 2
result = (int(AB) + int(C) + abs(int(AB) - int(C)))/2

print("The biggest number is %d" %result)