# Declare and initialize objects
fizz = "Fizz"
buzz = "Buzz"
fizz_buzz = "FizzBuzz"

# Print FizzBuzz based off the following conditions
for i in range(1, 100):
  if i%3 == 0 and i%5 != 0:
    print (fizz)
  elif i%3 != 0 and i%5 == 0:
    print(buzz)
  elif i%3 == 0 and i%5 == 0:
    print(fizz_buzz)
  else:
    print(i)
