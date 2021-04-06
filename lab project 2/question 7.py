#game finder a secret number within 3 attempts using while loop
x=7
i=3

while i!=0:
    guess = int(input("enter the num"))
    if guess==x:
        print("correct")
        break
    else:
        print ("try again")
    i-=1
    