pesos = int(input('What do you have left in pesos? '))
soles = int(input('What do you have left in soles? '))
reais = int(input('What do you have left in reais? '))

p = pesos * 0.00025
s = soles * 0.27
r = reais * 0.20

dollars = p + s + r
print(dollars)
