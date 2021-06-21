N = int(input())
if N%2 == 0:
    print("EVEN ",end="")
    if N > 0 :
        print("POSITIVE")
    elif N < 0 :
        print("NEGATIVE")
elif N%2 != 0:
    print("ODD ",end="")
    if N > 0:
        print("POSITIVE")
    elif N < 0:
        print("NEGATIVE")
elif N == 0:
    print("NULL")