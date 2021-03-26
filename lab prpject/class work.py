#write a program to see a number given by the user is armstrong number or not
num=int(input("enter number to see if it is armstrong or not"))
c=num
sum=0
while num>0:
    rem=num%10
    sum=sum+(rem**3)
    num=num//10
if sum==c:
    print("yes")
else:
    print("no")