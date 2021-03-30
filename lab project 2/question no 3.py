#price of a house is $1m.If a buyer has good credit, they need to put down 10% otherwise they
#have to put 20%. print the dow payment

price=1000000
has_good_credit=True

if has_good_credit:
    downpayment=0.1*price
else:
    downpayment=0.2*price

print(f"downpayment= ${downpayment}")
