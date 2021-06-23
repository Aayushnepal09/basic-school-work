'''write a python function to find the max of three number '''
a=int(input("enter the first number "))
b=int(input("enter the second number"))
c=int(input("enter the thrd number "))

def max(a,b,c):
    if a>b and a>c:
        print(f"{a} is the greater number ")
    elif b>a and b>c:
        print(f"{b}is the greater number")
    else:
        print(f"{c}is the greater number ")

max(a,b,c)
