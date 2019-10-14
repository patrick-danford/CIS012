# CIS012 Assignment 06_2
# Patrick Danford, 10/13/2019

while True:
    # Prompt user for input
    instr = input("Enter a string with two \"!\" surrounding portion of the string: ")

    # Locate first '!'
    bang1 = instr.find('!')

    # Create new string with characters occurring after first '!'
    substr = instr[bang1 + 1:]

    # Locate second '!'
    bang2 = substr.find('!')

    # Create new string ending at second '!'
    newstr = substr[:bang2]

    # Print new string in reverse order
    print(newstr[::-1])

    # Prompt user to go again, or end
    again = input('Do you wish to repeat this program? (y / n) ')
    if again == 'y':
        continue
    else:
        print('Thank you for playing.')
        break