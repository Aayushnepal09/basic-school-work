#If name is less than 3 characters long name - must be at least thee characters other wise if its more
#than 50 characters than max number of characters is 50 other wise name looks good

name=input("enter your name ")
count=len(name)
if count<3:
    print("name should be at least 3 words ")
elif count>50:
    print("name is too long" )
else:
    print(("name looks good"))
    