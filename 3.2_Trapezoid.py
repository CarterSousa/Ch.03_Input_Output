'''
TRAPEZOID PROGRAM
-------------------
Create a new program that will ask the user for the information needed to find the area of a trapezoid, and then print the area.

Test with the following:

base 1: 2       base 2: 3    height: 4    area: 10
base 1: 5       base 2: 7    height: 2    area: 12
base 1: 1       base 2: 2    height: 3    area: 4.5
base 1: 7       base 2: 2    height: 4    area: 18
'''
base_1 = int(input("What is base 1 of the trapazoid?: "))
base_2 = int(input("What is base 2 of the trapazoid?: "))
height = int(input("What is the height of the trapazoid?: "))
area = (base_1+base_2)/2*height
print(" Area of the trapizoid is:",area,"m2")
