#it the temprature is greater than 30, its a hot day other wise if its less than 10,
#its a cold day,otherwise, its neither hor nor cold.

temperature=float(input("enter he temperature "))
if temperature>30:
    print("its a hot day ")
elif temperature<10:
    print("its a cold day")
else:
    print("its neither hot nor cold")