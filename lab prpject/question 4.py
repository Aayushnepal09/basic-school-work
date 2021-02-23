#n students takes k apple and distribute them among each others evenly. the remending ( the undivisible part remending
#in the basket. how many apple will remain in the basket? the program reads the number of n and k. it should
#print two answer fo the above question
n= int(input(" enter the number of student"))
k=int(input("enter the number of apple "))
take= k/n
remain=(k-take)
print (" the number of apple they get is ",take)
print("the reminding is ",remain)