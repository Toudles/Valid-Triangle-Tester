"""
Assignment #3, Part 1
Andrew Park
"""

import math

print("Valid Triangle Tester")
print()
#get the values of the points 
p1x = float(input("Enter Point #1 - x position: "))
p1y = float(input("Enter Point #1 - y position: "))
p2x = float(input("Enter Point #2 - x position: "))
p2y = float(input("Enter Point #2 - y position: "))
p3x = float(input("Enter Point #3 - x position: "))
p3y = float(input("Enter Point #3 - y position: "))

#calculate the side lengths
side1 = format(math.sqrt(((p1x - p2x)**2 + (p1y - p2y)**2)), ".2f")
side2 = format(math.sqrt(((p3x - p1x)**2 + (p3y - p1y)**2)), ".2f")
side3 = format(math.sqrt(((p3x - p2x)**2 + (p3y - p2y)**2)), ".2f")

print()

print("The length of each side of your test shape is: ")
print()
print("Side 1:", (side1))
print("Side 2:", (side2))
print("SIde 3:", (side3))

print()

#see if the sides make a triangle
#made them floats because it would concatnate strings together instead of the numbers,
if ((float(side1) + float(side2)) > float(side3)) and ((float(side2) + float(side3)) > float(side1)) and ((float(side3) + float(side1)) > float(side2)):
    print("This is a valid triangle!")
    Triangle = True
else:
    print("This is not a valid triangle!")
    Triangle = False
    #ends the code if it is not a valid triangle


#test the type of triangle it is

#equliateral
if Triangle == True:
    if (side1 == side2 == side3):
        print("This is an equilateral triangle")
#add isosceles here because the way i did it, it would say it's isosceles if it was equilateral so
#added an elif that if it's not all equal but there are 2 equal sides, it would be isosceles.
    elif (side1 == side2) and (side2 == side1) or (side3 == side2) and (side2 == side3) or (side3 == side1) and (side1 == side3):
        print("This is an isosceles triangle.")


#scalene triangle
if Triangle == True:
    if (side1 != side2 != side3):
        scalene = True
        print("This is a scalene triangle")


#right triangle
#test if pythagorean theorem holds true

#change variable according to all possible scenarios of every side being the largest 
if Triangle == True:
    if side3 > side1 and side2:
    
    #if side3 is the largest, perform theorem to see if true
    #put float because it would be a string if i didn't
        if round(float(side1)**2) + round(float(side2)**2) == round(float(side3)**2):
            right = True
            print("This is also a right triangle")

    elif side1 > side2 and side3:

    #if side1 is the largest, perform theorem to see if true
        if round(float(side2)**2) + round(float(side3)**2) == round(float(side1)**2):
            right = True
            print("This is also a right triangle")

    elif side2 > side1 and side3:

    #if side2 is the largest, perform theorem to see if true
        if round(float(side3)**2) + round(float(side1)**2) == round(float(side2)**2):
            print("This is also a right triangle")
            right = True


