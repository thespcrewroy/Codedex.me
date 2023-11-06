# Write code below 💖

# initialize relative gravity
relative_gravity = 0.00
destination_weight = 0.00

# Output a table of planets
print('Here are the planets and their corresponding politions.')
print('Number   Planet')
print('1        Mercury')
print('2        Venus')
print('3        Mars')
print('4        Jupiter')
print('5        Saturn')
print('6        Uranus')
print('7        Neptune')

# Prompt the user for the planet that they are on
planet = int(input('Which planet are you on?: '))

# Prompt the user for their weight
earth_weight = float(input('What is your Earth weight: '))

if planet == 1:
  relative_gravity = 0.38
elif planet == 2:
  relative_gravity = 0.91
elif planet == 3:
  relative_gravity = 0.38
elif planet == 4:
  relative_gravity = 2.53
elif planet == 5:
  relative_gravity = 1.07
elif planet == 6:
  relative_gravity == 0.89
elif planet == 7:
  relative_gravity == 1.14
else:
  print('Not a viable planet')

# Calculate the user's weight on the destination planet
destination_weight = earth_weight * relative_gravity

print(destination_weight)
