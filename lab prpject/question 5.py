# give the intger n- the number of minutes that have passed since midnight - how man hours and minutes
# are displayed on 24th digital clock?
n=int(input("enter the minutes passed since midnight:"))
hours=(n/60)
minutes=(n%60)
print(f"the hours is {minutes}")
print(f"the minutes is {minutes }")
print(f" its {hours}:{minutes} now")
