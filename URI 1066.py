i = 0
even = 0
odd = 0
pos = 0
neg = 0
while i<5 :
    num = int(input())
    if num%2 == 0:
        even = even+1
    if num%2 != 0 :
        odd = odd+1
    if num > 0:
        pos = pos+1
    if num < 0:
        neg = neg+1
    i = i+1

print("%d valor(es) par(es)" %even)
print("%d valor(es) impar(es)" %odd)
print("%d valor(es) positivo(s)" %pos)
print("%d valor(es) negativo(s)" %neg)