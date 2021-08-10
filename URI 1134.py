alcohol = 0
gasoline = 0
diesel = 0
flag = 0
while flag == 0 :
    fuel = int(input())
    if fuel == 1:
        alcohol += 1
    elif fuel == 2:
        gasoline += 1
    elif fuel == 3:
        diesel += 1
    elif fuel == 4:
        break
    else:
        continue
print("MUITO OBRIGADO")
print("Alcool: %d" %alcohol)
print("Gasolina: %d" %gasoline)
print("Diesel: %d" %diesel)
