# CIS012 Assignment 08_1
# Patrick Danford, 11/3/2019

# Loop that initializes lists and takes input from user
while True:
    wrdlist = list()
    newlist = list()
    fname = input("Enter file name: ")
    # If valid file proceed, if entry invalid quit
    try:
        fhand = open(fname)
    except:
        print("File not found, please enter correct file name.")
        quit()
    # Loop that strips newlines, converts to lower case, then creates new list of all words in the file
    for line in fhand:
        line = line.strip()
        line = line.lower()
        words = line.split()
        wrdlist = wrdlist + words
    # Sort new list in alphabetical order
    wrdlist.sort()
    # Loop that puts unique values from wrdlist into a new list
    for cnt in wrdlist:
        if cnt not in newlist:
            newlist.append(cnt)
    # Output new sorted list and count of unique values
    print(newlist)
    print("File", fname, "has", len(newlist), "different words.")
    # Prompt user to go again, break if no
    again = input('Do you want to try again? (y/n): ')
    if again == 'y':
        continue
    else:
        print('Thank you for playing.')
        break