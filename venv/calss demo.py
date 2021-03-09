# wirte a program to take a inout from the user,ask the user age. If the use age is below 15
#print a message "you are a child", if the users age is greater then 15 and less then 40
#print a message "you are a adult", if the users age then print a message "you are old"
age=int(input("enter your age "))
if age<15:
    print("you are a child")
elif age>15 and age<40:
    print("you are an adult")
elif age>40:
    print("you are old")

    