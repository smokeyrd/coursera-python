"""
Template - Compute whether an integer is even.
"""

###################################################
# Is even formula
# Student should enter function on the next lines.

def is_even(number):
    if (number%2==0):
        return True
    else:
        return False


###################################################
# Tests
# Student should not change this code.

number = 8
if is_even(number):
    print(number, "is even.")
else:
    print(number, "is odd.")

number = 3
if is_even(number):
    print(number, "is even.")
else:
    print(number, "is odd.")

number = 12
if is_even(number):
    print(number, "is even.")
else:
    print(number, "is odd.")

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# 8 is even.
# 3 is odd.
# 12 is even.
