dollars = input("How many dollars do you have?:" )
dollars = float(dollars)
value_peso = 0.050
pesos = dollars / value_peso
pesos = round(pesos, 2)
pesos = str(pesos)
print("You have $" + pesos + " mexican pesos")


