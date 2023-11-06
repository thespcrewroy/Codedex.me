import random

# Prompt the user to ask a question
input('Question: ')

answer = random.randint(1,9)  # generate a random number from 1 to 9

# Write a table that corresponds a number to an answer
if answer == 1:
  print('Magic 8 Ball: Yes - definitely.')
elif answer == 2:
  print('Magic 8 Ball: It is decidedly so.')
elif answer == 3:
  print('Magic 8 Ball: Without a doubt')
elif answer == 4:
  print('Magic 8 Ball: Reply hazy, try again.')
elif answer == 5:  
  print('Magic 8 Ball: Ask again later.')
elif answer == 6:
  print('Magic 8 Ball: Better not tell you now.')
elif answer == 7:
  print('Magic 8 Ball: My sources say no.')
elif answer == 8:
  print('Magic 8 Ball: Outlook not so good.')
elif answer == 9:
  print('Magic 8 Ball: Very doubtful.')
