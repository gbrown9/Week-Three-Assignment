_author_ = "Gabe Brown"

# Program - StarWars Name
# CIS - 125
# Has the user input info and computes StarWars name


# Get input from users
first = input("What is your FIRST Name? ")
last = input("What is your LAST Name? ")
maiden = input("What is your Mother's Maiden Name? ")
city = input("What is the Town you were born in? ")

# Compute StarWars Name
swfirst = last[0:3] + first[0:2]
swlast = maiden[0:2] + city[0:3]

# Print out StarWars Name
print("Your StarWars name is:", swfirst, swlast)