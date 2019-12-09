inStock = ([range(10)], [range(4)])  # 2D list (row size:10, column size:4)
alpha = list(range(20))  # 1D list with 20 elements.
beta = list(range(20))  # 1D list with 20 elements.
gamma = [11, 13, 15, 17]
delta = [3, 5, 2, 6, 10, 9, 7, 11, 1, 8]


# print(alpha)
# print(beta)

def setZero(zerolst):
    for item in range(len(zerolst)):
        zerolst[item] = 0
    return zerolst


print(setZero(alpha))
print(setZero(beta))


def inputArray(inlst):
    nums = 1
    for item in range(len(inlst)):
        inp = input("Enter 20 integers. Number " + str(nums) + ': ')
        nums = nums + 1
        inlst[item] = inp
    return inlst


print(inputArray(alpha))

# def doubleArray(doublst):
#   doublst = alpha.copy()
#   for item in range(len(doublst)):
#    doublst[item] *= 2
# return doublst

print(beta)


def double(b, a):
    for i in b:
        b[i] = [i * 2 for i in a]


print(double(beta, alpha))
