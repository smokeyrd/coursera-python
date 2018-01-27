"""
Template - compute the distance between the points (x0, y0) and (x1, y1).
"""

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

# Test 1 - Select the following lines and use ctrl+shift+k to uncomment.
x_0 = 2
y_0 = 2
x_1 = 5
y_1 = 6


# Test 2 - Select the following lines and use ctrl+shift+k to uncomment.
#x_0 = 1
#y_0 = 1
#x_1 = 2
#y_1 = 2


# Test 3 - Select the following lines and use ctrl+shift+k to uncomment.
#x_0 = 0
#y_0 = 0
#x_1 = 3
#y_1 = 4


###################################################
# Distance formula
# Student should enter formula on the next line.

# Hint: You need to use the power operation ** .
distance= ((x_0-x_1)**2+(y_0-y_1)**2)**.5

###################################################
# Test output
# Student should not change this code.

print("The distance from (" + str(x_0) + ", " + str(y_0) +
      ") to (" + str(x_1) + ", " + str(y_1) + ") is " + str(distance) + ".")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#The distance from (2, 2) to (5, 6) is 5.0.

# Test 2 output:
#The distance from (1, 1) to (2, 2) is 1.41421356237.

# Test 3 output:
#The distance from (0, 0) to (3, 4) is 5.0.
