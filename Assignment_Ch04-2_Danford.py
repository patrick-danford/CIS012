# CIS012 Assignment 04_2
# Patrick Danford, 9/28/2019


# Function that compares three input numbers, returns them in ascending order
def NumAscend(num1, num2, num3):
    if num1 < num2 < num3:
        print("Here are the numbers in ascending order:", num1, num2, num3)

    elif num1 < num3 < num2:
        print("Here are the numbers in ascending order:", num1, num3, num2)

    elif num2 < num1 < num3:
        print("Here are the numbers in ascending order:", num2, num1, num3)

    elif num2 < num3 < num1:
        print("Here are the numbers in ascending order:", num2, num3, num1)

    elif num3 < num2 < num1:
        print("Here are the numbers in ascending order:", num3, num2, num1)

    elif num3 < num1 < num2:
        print("Here are the numbers in ascending order:", num3, num1, num2)


# User inputs required information
in1 = int(input("Enter first number: "))
in2 = int(input("Enter second number: "))
in3 = int(input("Enter third number: "))

# Invoke def NumAscend
NumAscend(in1, in2, in3)
