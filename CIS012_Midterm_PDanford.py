# CIS012 Midterm programming
# Patrick Danford, 10/16/2019

# Loop that initializes variables and takes input from user
while True:
    count = 0
    vowel = 0
    nums = 0
    alpha = 0
    space = 0
    instr = input("Please enter a sentence: ")
    # Loop that tests each input character to determine what it is then creates count
    for n in instr:
        count = count + 1
        if n.isdigit():
            nums = nums + 1
        elif n.isalpha():
            alpha = alpha + 1
        elif n.isspace():
            space = space + 1
        if n == 'a':
            vowel = vowel + 1
        elif n == 'A':
            vowel = vowel + 1
        elif n == 'e':
            vowel = vowel + 1
        elif n == 'E':
            vowel = vowel + 1
        elif n == 'i':
            vowel = vowel + 1
        elif n == 'I':
            vowel = vowel + 1
        elif n == 'o':
            vowel = vowel + 1
        elif n == 'O':
            vowel = vowel + 1
        elif n == 'u':
            vowel = vowel + 1
        elif n == 'U':
            vowel = vowel + 1
    # Output counts of different characters
    print("Your sentence has", count, "characters")
    print("Your sentence has", vowel, "vowels")
    print("Your sentence has", alpha - vowel, "consonants")
    print("Your sentence has", nums, "numbers")
    print("Your sentence has", space, "spaces")
    print("Your sentence has", count - (nums + alpha + space), "non-alphanumeric characters")
    again = input('Do you want to try again? (y/n): ')
    # Prompt user to go again, break if no
    if again == 'y':
        continue
    else:
        print('Thank you for playing.')
        break
