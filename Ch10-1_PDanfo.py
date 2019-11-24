# CIS012 Assignment 10_1
# Patrick Danford, 11/23/2019

# Loop that takes input from user
while True:
    fname = input("Please enter file name to process: ")
    # If valid file proceed, if entry invalid return to beginning of loop
    try:
        fhand = open(fname)
    except:
        print("File name", fname, "does not exist. Please enter correct file name.")
        continue
    # Separate file into individual letters, initialize dictionary
    letters = fhand.read()
    counts = dict()
    # Loop that converts to lower case. If alphanumeric, add to the dictionary
    for letter in letters:
        letter = letter.lower()
        if letter.isalpha():
            counts[letter] = counts.get(letter, 0) + 1
    # Create list, loop through dictionary and put chars & counts into a tuple, val first
    lst = list()
    for key, val in counts.items():
        kvtup = (val, key)
        lst.append(kvtup)
    # Sort list, print
    lst = sorted(lst)
    print(lst)
    # Prompt user to go again, break if no
    again = input('Do you want to try another file? (y/n): ')
    if again == 'y':
        continue
    else:
        print('Thank you for playing.')
        break


