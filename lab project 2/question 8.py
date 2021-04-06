""" car game
 >help
start-to start the car
 stop- to stop yhe car
 quit- to exit
 >asd
 i don't under stand this
 > start
 car started.... ready to go!!
 >stop
 car stopped
 >quit"""

command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started !!")
        else:
            started = True
            print("Car started !!...")
    elif command == "stop":
        if not started:
            print("Car is already stopped !!")
        else:
            started = False
            print("Car stopped !!..")
    elif command == "help":
        print(""" start - to start the car stop - to stop the car quit - to exit  """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that !!")
