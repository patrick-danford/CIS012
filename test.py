x = int(input("enter first number: "))
y = int(input("enter second number: "))
z = int(input("enter third number: "))

if x < y < z:
    print(x, y, z)

elif x < z < y:
    print(x, z, y)

elif y < x < z:
    print(y, x, z)

elif y < z < x:
    print(y, z, x)

elif z < y < x:
    print(z, y, x)

elif z < x < y:
    print(z, x, y)
