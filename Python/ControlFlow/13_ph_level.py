ph = int(input('Input a pH value between 0 and 14: '))
if ph > 7:
  print('Basic')
elif ph < 7: 
  print('Acidic')
else:
  print('Neutral')
