# CIS012 Assignment 09_1
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
    # Separate file into individual letters, initialize dictionary
    letters = fhand.read()
    di = dict()
    # Loop that splits letters and puts them into dictionary
    for letter in letters:
        lets = letter.split()
        # print(lets)
        # Loop that counts numbers of each character and puts into dictionary
        for l in lets:
            # if l in di:
                # di[l] = di[l] + 1
            # else:
                # di[l] = 1
            di[l] = di.get(l, 0) + 1
        # print(l, di[l])
    # Print out the dictionary
    print(di)
    # Prompt user to go again, break if no
    again = input('Do you want to try again? (y/n): ')
    if again == 'y':
        continue
    else:
        print('Thank you for playing.')
        break
