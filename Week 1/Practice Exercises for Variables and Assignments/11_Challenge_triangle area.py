"""
Template - Compute the area of a triangle (using Heron's formula),
       given its side lengths.
"""

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

# Test 1 - Select the following lines and use ctrl+shift+k to uncomment.
x_0, y_0 = 0, 0
x_1, y_1 = 3, 4
x_2, y_2 = 1, 1


# Test 2 - Select the following lines and use ctrl+shift+k to uncomment.
#x_0, y_0 = -2, 4
#x_1, y_1 = 1, 6
#x_2, y_2 = 2, 1


# Test 3 - Select the following lines and use ctrl+shift+k to uncomment.
#x_0, y_0 = 10, 0
#x_1, y_1 = 0, 0
#x_2, y_2 = 0, 10


###################################################
# Triangle area (Heron's) formula
# Student should enter formulas on the next lines.

#Calculate side lengths
distance1= ((x_0-x_1)**2+(y_0-y_1)**2)**.5
distance2= ((x_1-x_2)**2+(y_1-y_2)**2)**.5
distance3= ((x_2-x_0)**2+(y_2-y_0)**2)**.5

#Semi-Perimeter
semi_perimeter=.5*(distance1+distance2+distance3)

#Area
area= (semi_perimeter*(semi_perimeter-distance1)*(semi_perimeter-distance2)*(semi_perimeter-distance3))**.5

###################################################
# Test output
# Student should not change this code.

print("A triangle with vertices (" + str(x_0) + "," + str(y_0) + ")," +
      "(" + str(x_1) + "," + str(y_1) + "), and" +
      "(" + str(x_2) + "," + str(y_2) + ") has an area of " + str(area) + ".")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#A triangle with vertices (0,0), (3,4), and (1,1) has an area of 0.5.

# Test 2 output:
#A triangle with vertices (-2,4), (1,6), and (2,1) has an area of 8.5.

# Test 3 output:
#A triangle with vertices (10,0), (0,0), and (0,10) has an area of 50.0.