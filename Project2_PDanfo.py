# CIS012 Extra credit "Project 2"
# Patrick Danford, 12/8/2019

# Import regex
import re

# Overall loop for user to input file name
while True:
    fname = input("Please enter the file name to search: ")
    # Loop for user to input specific word
    while True:
        # Dictionary to store word and their frequencies
        counts = dict()
        # If valid file proceed, if entry invalid break to outer loop and prompt user again
        try:
            fhand = open(fname.lower())
            testinp = input("Please enter the word to search in the file " + fname + ": ")
        except:
            print("File name", fname, "does not exist.")
            break
        # Loop that uses regex to break file into lines & words, removes any non alphabet characters
        for line in fhand:
            line = re.sub(r'[^a-zA-Z0-9 ]', r'', line.lower())
            # print(line)
            line = re.findall(r'\w+', line)
            # Loop that counts the words and stores frequencies in dictionary.
            for word in line:
                if word in counts:
                    counts[word] += 1
                else:
                    counts[word] = 1
        # print(counts)
        # Output requested word count or state that the word does not exist
        if testinp in counts:
            print("The word \"" + testinp + "\" appears", counts[testinp], "times in the file.")
        else:
            print("The word \"" + testinp + "\" does not appear in the file.")
        # Prompt user to go again, break to outer loop if no
        anotherword = input('Do you want to search for more words? (y/n): ')
        if anotherword == 'y':
            continue
        else:
            break
    # Prompt user to go again, break to no
    again = input('Do you want to try another file? (y/n): ')
    if again == 'y':
        continue
    else:
        print('Thank you for using "word Search" program.')
        break
