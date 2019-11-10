# CIS012 Assignment 09_2
# Patrick Danford, 11/9/2019

# Loop that takes input from user
while True:
    fname = input("Please enter file name to process: ")
    # If valid file proceed, if entry invalid return to beginning of loop
    try:
        fhand = open(fname)
    except:
        print("File name", fname, "does not exist. Please enter correct file name.")
        continue
    # Initialize dictionary
    di = dict()
    # Loop that strips whitespace, converts to lowercase, and splits lines into individual words
    for line in fhand:
        line = line.strip()
        line = line.lower()
        words = line.split()
        # Loop that counts numbers of each word and puts into dictionary
        for w in words:
            di[w] = di.get(w, 0) + 1
    # Print dictionary, and statement that indicates total number of words
    print(di)
    print("File", fname, "has", len(di), "different words.")
    # Prompt user to go again, break if no
    again = input('Do you want to try another file? (y/n): ')
    if again == 'y':
        continue
    else:
        print('Thank you for playing.')
        break
