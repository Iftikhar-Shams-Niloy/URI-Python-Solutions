num = float(input())
if num >= 0 and num <= 2000.00:
    print("Isento")
elif num >= 2000.01 and num <= 3000.00:
    result1 = (num-2000)*(0.08)
    print("R$ %.2f" %result1)
elif num >= 3000.01 and num <= 4500.00:
    result2 = (1000*0.08)+((num-3000)*0.18)
    print("R$ %.2f" %result2)
elif num > 4500.00:
    result3 = (1000*0.08)+(1500*.18)+((num-4500)*0.28)
    print("R$ %.2f" %result3)