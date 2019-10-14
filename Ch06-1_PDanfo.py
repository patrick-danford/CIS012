# CIS012 Assignment 06_1
# Patrick Danford, 10/13/2019

# Prompt user for input
instr = input("Enter a string with a colon and a number after it: ")

# Find the colon in the input string
ipos = instr.find(':')
# print(ipos)

# Put numerals after the colon into a new variable
numstr = instr[ipos + 1:]
# print(numstr)

# Convert string to float, put into new variable
numflt = float(numstr)
# print(numflt)

# Add 2.0 to the float and print the result
print("Extracted a number from given string and added 2.0 to it: ", numflt + 2.0)
