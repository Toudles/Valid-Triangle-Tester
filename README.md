1) Prompt the user to enter in 3 points on a standard Cartesian coordinate plane. You can assume the user will enter these values as floating point numbers.
2) Compute the distance between each points - you will be computing 3 distance values. Use the distance formula to do this:
    ( (x1-x2)2 + (y1-y2)2 ) 0.5

    ... note that you can raise a value to the 0.5 power to compute the square root, or you can use the sqrt() function in the math module - your choice!
3) Report the distance to the user of each side, rounded to 2 decimal places
4) Next, determine if the three points could form a valid triangle. You can assume that the triangle is valid by checking the following. Note that ALL THREE of these conditions must be met in order for a triangle to be valid):
    (a) Side 1 + Side 2 must be longer than Side 3
    (b) Side 2 + Side 3 must be longer than Side 1
    (c) Side 3 + Side 1 must be longer than Side 2
5) If the triangle is valid, report whether it is an equilateral, isosceles, or scalene triangle:
Equilateral Triangle: all sides of the triangle have the same length
Isosceles Triangle: only two sides of the triangle have the same length
Scalene Triangle: all sides of the triangle have different lengths
Right Triangle: It has one angle of 90 degrees. You can do this by using the Pythagorean Theorem on the sides of the triangle - a2 + b2 = c2.
