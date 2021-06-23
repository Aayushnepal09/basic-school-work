'''write a function called fizz_buzz that takes a number.
if the number is divisible by 3, it should return "fizz"
if it is divisible by 5 return "BUZZ"
if it is divisible by 3 and 5 then return "fizz buzz"
otherwise return same number'''
num=int(input("enter the number "))
def fizz_buzz(num):
    if num%3==0 and num%5==0:
        return "fizz buzz"
    elif num%3==0 and num%5!=0:
        return"fizz"
    elif num%5==0 and num%3!=0:
        return"buzz"
    else:
        return num
print(fizz_buzz(num))