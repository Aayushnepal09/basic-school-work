"'give a three digit number and find its digit sum"""
def getSum(n):
    sum = 0
    while (n != 0):
        sum = sum + int(n % 10)
        n = int(n // 10)

    return sum


# Driver code
n =int(input("enter a number"))
print(getSum(n))

