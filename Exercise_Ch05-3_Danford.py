# CIS012 Assignment 05_3
# Patrick Danford, 10/06/2019

# Initialize variables for loop
even = 0
odd = 0
small = None
large = None

# Loop that cycles through list, determines smallest, largest, odd, even numbers
for i in [3, 8, 5, 1, 4, 9, 2, 10, 7]:
    if small is None:
        small = i
        # print('Small', small)
    elif i < small:
        small = i
        # print('Small', small)
    if large is None:
        large = i
        # print('Large', large)
    elif i > large:
        large = i
        # print('Large', large)
    if (i % 2) == 0:
        # print('Even', i)
        even = even + i
    else:
        # print('Odd', i)
        odd = odd + i

# Print out sum of even and sum of odd numbers
print('Sum of even numbers is: ', even)
print('Sum of odd numbers is: ', odd)
# Print out smallest and largest numbers
print('Largest number in the list is: ', large)
print('Smallest number in the list is: ', small)
