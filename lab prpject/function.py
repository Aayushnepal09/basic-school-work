
num=int(input("enter the number for mul"))
def mul(num):

    product=1
    for i in range (1,11):
        product=num*i
        print (num,"*",i,"=",product)

mul(num)