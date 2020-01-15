#Joseph Sherry
#Lab 1C
############################
#keepGoing          boolean loop vatiable
#maxCapacity        maximum room capacity based on user input
#plannedAttendance  planned attendees based on user input
#userInput          the user input as a string
#capacity           function parameter of user input room capacity carried over from capacity()
#attendees          function parameter of user input room capacity carried over from attendees()
#difference         stores return from register()
def capacity():#would normally call this getCapacity
    return int(input("Enter the maximum capacity of the room: "))
def attendees():#would normally call this getAttendees
    return int(input("How many people want to attend the event?: "))
def register(capacity : int, atendees : int):#don't like this name at all maybe processInputs or something
    return capacity - atendees
def loopTest():
    x = 1
    while(x == 1):
        userInput = input("Do you have more data to input (y/n)?").lower()
        if(userInput == "y" or userInput == "n"):
            x = 8675309 #because I can't use break statements apparently would normally just use while(True) for sub-loop and break here
    return userInput == "y"

keepGoing = True
while (keepGoing):
    maxCapacity = capacity()
    plannedAttedance = attendees()
    difference = register(maxCapacity, plannedAttedance)
    if(difference >= 0):
        print("Legally ", (difference), " more people may attend your event")
    else:
        print("Legally ", (difference * -1), " people must be uninvited from your event")
    keepGoing = loopTest()