import random

user_input = 0

d1 = random.randint(1, 6)
d2 = random.randint(1, 6)
total = d1 + d2

while total != user_input:
  user_input = int(input('What is the total (2-12)? '))

print('You got it!')
