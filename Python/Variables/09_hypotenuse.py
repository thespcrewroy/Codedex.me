
a = int(input('Enter the length of leg 1/coefficient 1: '))
b = int(input('Enter the length of leg 2/coefficient 2: '))
c = int(input('Enter the constant for the polynomial: '))

print('Calculate the hypotenuse')
c = (a**2 + b**2)**0.5
print(c)

print('Quadratic Formula')
root1 = (-1*b + (b**2 - 4*a*c)**0.5)/(2*a)
root2 = (-1*b - (b**2 - 4*a*c)**0.5)/(2*a)
print(root1)
print(root2)
