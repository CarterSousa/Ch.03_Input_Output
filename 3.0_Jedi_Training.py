# Sign your name:Carter Sousa
# In all the short programs below, do a good job communicating with your end user!

# 1.) Write a program that asks someone for their name and then prints a greeting that uses their name.
import math

username = input("hello! What is you name: ")
print("hello "+username+" welcome to my calculation program!")

# 2. Write a program where a user enters a base and height and you print the area of a triangle.
base = input("What is the base of your triangle: ")
height = input("what is the height of your triangle: ")
area=int(1/2)(base*height)
print("The area of the triangle is:",area,)
# 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference.
radius = int(input(" What is the radius of the circle?: "))
circumference = 3.14 * radius*2
print("Circumference",circumference,)

# 4. Ask a user for an integer and then print the square root.
#
#
# 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma.
#    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next.
mass = int(input(" What is the mass?: "))
acceleration = int(input(" What is the acceleration?: "))
force = mass * acceleration
print(" Force = ",force," N")
print(" Get it? ")

