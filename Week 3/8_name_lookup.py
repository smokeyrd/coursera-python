"""
Template - Compute instructor's last name, given the first name.
"""

###################################################
# Name lookup formula
# Student should enter function on the next lines.

def name_lookup(first_name):
    if first_name==("Joe"):
        return "Warren"
    elif first_name==("Scott"):
        return "Rixner"
    elif first_name==("John"):
        return "Greiner"
    elif first_name==("Stephen"):
        return "Wong"
    else:
        return "Error: Not an instructor"
###################################################
# Tests
# Student should not change this code.

first_name = "Joe"
print(first_name + "'s last name is", name_lookup(first_name))

first_name = "Scott"
print(first_name + "'s last name is", name_lookup(first_name))

first_name = "John"
print(first_name + "'s last name is", name_lookup(first_name))

first_name = "Stephen"
print(first_name + "'s last name is", name_lookup(first_name))

first_name = "Mary"
print(first_name + "'s last name is", name_lookup(first_name))

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Joe's last name is Warren
# Scott's last name is Rixner
# John's last name is Greiner
# Stephen's last name is Wong
# Mary's last name is Error: Not an instructor
