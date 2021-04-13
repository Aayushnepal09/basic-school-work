#input the weight of a person in either kg or lbs.
#if the person provides his/her weight in kg then convert it into lbs else convert it to kg.

weight=(float(input("enter your weight")))
weight1=(input("is it in lbs of kg?"))
if weight1=="kg":
    convert=weight*2.21

    print(f"your weight in lbs= {convert}")
elif weight1=="lbs":
    convert=weight/2.21
    print(f'your weight in kg is{convert}')
else:
    print('i dont understand')


