# Declare and initialize objects
gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

# Prompt the user for the questions and add points based on answers

print('Q1) Do you like Dawn or Dusk? ')
print('1) Dawn')
print('2) Dusk')
q1 = int(input('Enter the corresponding number: '))

if q1 == 1:
  gryffindor += 1
  ravenclaw += 1
elif q1 == 2:
  hufflepuff += 1
  slytherin += 1
else:
  print('Wrong input for Q1.')

print("Q2) When I'm dead, I want people to remember me as: ")
print('1) The Good')
print('2) The Great')
print('3) The Wise')
print('4) The Bold')
q2 = int(input('Enter the corresponding number: '))

if q2 == 1:
  hufflepuff += 2
elif q2 == 2:
  slytherin += 2
elif q2 == 3:
  ravenclaw += 2
elif q2 == 4:
  gryffindor += 2
else:
  print('Wrong input for Q2.')

print('Q3) What kind of instrument most pleases your ear? ')
print('1) The violin')
print('2) The trumpet')
print('3) The piano')
print('4) The drum')
q3 = int(input('Enter the corresponding number: '))

if q3 == 1:
  slytherin += 4
elif q3 == 2:
  hufflepuff += 4
elif q3 == 3:
  ravenclaw += 4
elif q3 == 4:
  gryffindor += 4
else:
  print('Wrong input for Q3.')


# Determine the house
if gryffindor > ravenclaw and gryffindor > hufflepuff and gryffindor > slytherin:
  print('You are in Gryffindor!')
elif ravenclaw > gryffindor and ravenclaw > hufflepuff and ravenclaw > slytherin:
  print('You are in Ravenclaw!')
elif hufflepuff > gryffindor and hufflepuff > ravenclaw and hufflepuff > slytherin:
  print('You are in Hufflepuff!')
elif slytherin > gryffindor and slytherin > ravenclaw and slytherin > hufflepuff:
  print('You are in Slytherin!')
else:
  print('You do not strongly identify with any one house. You are not allowed at the Hogwarts School of Witchcraft and Wizardry.')
