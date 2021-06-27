ntimes = int(input())
for i in range(ntimes):
    nterms = int(input())
    n1, n2 = 0, 1
    count = 0
    if nterms == 1:
       print("Fib(1) = 1")
    else:
       while count < nterms:
           nth = n1 + n2
           n1 = n2
           n2 = nth
           count += 1
       print("Fib(%d) = %d"%(count,n1))