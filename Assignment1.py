# 1. Write a Python program to print the following string in a specific format (see the output).

print("Twinkle, twinkle, little star,")
print("\t How i wonder what you are!")
print("\t\tUp above the world so high,")
print("\t\tlike a diamond in the sky.")
print("Twinkle, Twinkle, little star,")
print("\t How i wonder what you are!")
print("\n")

# 2. Write a Python program to get the Python version you are using
import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)
print("\n")

# 3. Write a Python program to display the current date and time.
import time
print ("Current date and time :")
print(time.ctime())
print("\n")

# 4. Write a Python program which accepts the radius of a circle from the user and compute the area.
r =int(input("Input the radius of the circle "))
pi=3.14
area = float(pi*r**2)
print("The area of the circle with radius",area)
print("\n")

# 5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
first = input("What is your first name?")
last = input ("what is your last name?")
print (last,first)
print("\n")

# Write a python program which takes two inputs from user and print them addition

num1 = input('Enter first number: ')
num2 = input('Enter second number: ')
sum = float(num1) + float(num2)
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
print("\n")