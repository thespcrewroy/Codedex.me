number = int(input('Input an integer: '))
sum = 0
x = 1
count = 1

for x in range(0, number + 1):
  x = x**2
  sum += x
  count += 1
  x = count

print(sum)
