# CIS012 Assignment 07_1
# Patrick Danford, 10/26/2019

# Loop that initializes variables and takes input from user
while True:
    linecount = 0
    chars = 0
    cons = 0
    vset = set("aeiouAEIOU")
    vowels = 0
    nums = 0
    fname = input("Please enter file name: ")
    # If valid file proceed, if entry invalid quit
    try:
        fhand = open(fname)
    except:
        print("File cannot be opened, try again")
        quit()
    # Loop that counts lines of text in file
    for line in fhand:
        linecount = linecount + 1
    # Open file 2nd time to read in by character
    fhand2 = open(fname)
    inp = fhand2.read()
    # Loop that counts characters and numbers in the file
    for n in inp:
        if n in vset:
            vowels = vowels + 1
        elif n.isalpha():
            chars = chars + 1
        elif n.isnumeric():
            nums = nums + 1
    # Output counts of different characters
    print("File", fname, "has", linecount, "lines.")
    # print("File", fname, "has", chars, "total alphabetic characters.")
    print("File", fname, "has", vowels, "vowels.")
    print("File", fname, "has", chars - vowels, "consonants.")
    print("File", fname, "has", nums, "numbers.")
    again = input('Do you want to try again? (y/n): ')
    # Prompt user to go again, break if no
    if again == 'y':
        continue
    else:
        print('Thank you for playing.')
        break
