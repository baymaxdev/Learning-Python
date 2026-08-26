#Boolean
print(True)
print(False)

print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)

# Excercise
age = 20
height = 1.93
complexity = 1 + 2j

a = 10
b = 5  
print("a = 10 , b = 5")
print("a == b" , a == b)
print("a != b" , a != b)
print("a > b" , a > b)
print("a < b" , a < b)
print("a >= b" , a >= b)
print("a <= b" , a <= b)
print("a is b" , a is b)
print("a is not b" , a is not b)

num = int(input('Enter a number: '))
print(num, num**0, num**1, num**2, num**3)


base = float(input('Enter the Length of The Base: '))
rectHeight = float(input('Enter the Height of The Rectangle: '))
area = base * rectHeight
perimeter = 2 * (base + rectHeight)
print('The area of the rectangle is: ', int(area))
print('The perimeter of the rectangle is: ', int(perimeter))