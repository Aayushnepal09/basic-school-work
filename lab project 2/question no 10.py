"'write a python program to find the sum of three given integer.however, if two values are " \
"equal the sum is 0"
def sum (a,b,c):
    if a==b or b==c or c==a:
        sum = 0
    else:
        sum(a+b+c)
        return sum

x,y,z=[int(a)for a in input("enter three numbers:").split(",")]
print(sum(x,y,z))