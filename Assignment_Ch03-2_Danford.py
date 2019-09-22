# User inputs required information
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
num3 = int(input("enter third number: "))

# Compare numbers to determine what order they should go int.  Print
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
