# CIS012 Assignment 05_2
# Patrick Danford, 10/06/2019

#
print('Please enter six integers: ')
num1 = int(input("1.> "))
num2 = int(input("2.> "))
num3 = int(input("3.> "))
num4 = int(input("4.> "))
num5 = int(input("5.> "))
num6 = int(input("6.> "))

even = 0
odd = 0
for i in [num1, num2, num3, num4, num5, num6]:
    if (i % 2) == 0:
        # print('Even', i)
        even = even + i
    else:
        # print('Odd', i)
        odd = odd + i

print('Even sum is: ', even)
print('Odd sum is: ', odd)

print('Do you wish to repeat this program? (y / n) ')


