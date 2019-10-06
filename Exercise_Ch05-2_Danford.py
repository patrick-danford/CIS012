# CIS012 Assignment 05_2
# Patrick Danford, 10/06/2019

# Overall Loop that prompts user to input six integers
while True:
    print('Please enter six integers: ')

    # Initialize variables for next loop
    even = 0
    odd = 0
    n = 0
    # Loop that reads in integers, determines it they're odd or even, then totals the sum of each.
    while n < 6:
        # Read in if int
        try:
            num = int(input("> "))
            if (num % 2) == 0:
                # print('Even', i)
                even = even + num
                n = n + 1
            else:
                # print('Odd', i)
                odd = odd + num
                n = n + 1
        # If input not int prompt user to try again
        except:
            print('Invalid entry. Try again.')
            continue
    # Print totals of odd and even inputs
    print('Even sum is: ', even)
    print('Odd sum is: ', odd)

    # Prompt user to go again, or end
    again = input('Do you wish to repeat this program? (y / n) ')
    if again == 'y':
        continue
    else:
        print('Done!')
        break
