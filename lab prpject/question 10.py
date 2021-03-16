#write a python rogram to convert seconds to day , hour, minute and second
second=int(input("enter the value of second"))
day=(((second//60)//60)//24)

hour=((second//60)//60)
print(f"total hour for given seconds:{hour}")

minute=(second//60)
print(f"total minute for given second {minute}")