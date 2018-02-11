"""
Template - Compute whether two intervals intersect.
"""

###################################################
# Interval intersection formula
# Student should enter function on the next lines.
def interval_intersect(int1_lower, int1_upper, int2_lower, int2_upper):
    return (int2_lower<=int1_upper) and (int1_lower<=int2_upper)

###################################################
# Tests
# Student should not change this code.

int1_lower, int1_upper, int2_lower, int2_upper = 0, 1, 1, 2
print("Intervals [" + str(int1_lower) + ", " + str(int1_upper) + "] and [" +
      str(int2_lower) + ", " + str(int2_upper) + "] ", end="")
if interval_intersect(int1_lower, int1_upper, int2_lower, int2_upper):
    print("intersect.")
else:
    print("do not intersect.")

int1_lower, int1_upper, int2_lower, int2_upper = 1, 2, 0, 1
print("Intervals [" + str(int1_lower) + ", " + str(int1_upper) + "] and [" +
      str(int2_lower) + ", " + str(int2_upper) + "] ", end="")
if interval_intersect(int1_lower, int1_upper, int2_lower, int2_upper):
    print("intersect.")
else:
    print("do not intersect.")

int1_lower, int1_upper, int2_lower, int2_upper = 0, 1, 2, 3
print("Intervals [" + str(int1_lower) + ", " + str(int1_upper) + "] and [" +
      str(int2_lower) + ", " + str(int2_upper) + "] ", end="")
if interval_intersect(int1_lower, int1_upper, int2_lower, int2_upper):
    print("intersect.")
else:
    print("do not intersect.")

int1_lower, int1_upper, int2_lower, int2_upper = 2, 3, 0, 1
print("Intervals [" + str(int1_lower) + ", " + str(int1_upper) + "] and [" +
      str(int2_lower) + ", " + str(int2_upper) + "] ", end="")
if interval_intersect(int1_lower, int1_upper, int2_lower, int2_upper):
    print("intersect.")
else:
    print("do not intersect.")

int1_lower, int1_upper, int2_lower, int2_upper = 0, 3, 1, 2
print("Intervals [" + str(int1_lower) + ", " + str(int1_upper) + "] and [" +
      str(int2_lower) + ", " + str(int2_upper) + "] ", end="")
if interval_intersect(int1_lower, int1_upper, int2_lower, int2_upper):
    print("intersect.")
else:
    print("do not intersect.")

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Intervals [0, 1] and [1, 2] intersect.
# Intervals [1, 2] and [0, 1] intersect.
# Intervals [0, 1] and [2, 3] do not intersect.
# Intervals [2, 3] and [0, 1] do not intersect.
# Intervals [0, 3] and [1, 2] intersect.