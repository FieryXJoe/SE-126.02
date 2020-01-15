#Joseph Sherry
#Lab 1B
############################
#keepGoing          boolean loop vatiable
#maxCapacity        maximum room capacity based on user input
#plannedAttendance  planned attendees based on user input
#userInput          the user input as a string
#x                  gross variable because I cant break
keepGoing = True
while (keepGoing):
    maxCapacity = int(input("Enter the maximum capacity of the room: "))
    plannedAttedance = int(input("How many people want to attend the event?: "))
    if(maxCapacity >= plannedAttedance):
        print("Legally ", (maxCapacity - plannedAttedance), " more people may attend your event")
    else:
        print("Legally ", (plannedAttedance - maxCapacity), " people must be uninvited from your event")
    x = 1
    while(x == 1):
        userInput = input("Do you have more data to input (y/n)?").lower()
        if(userInput == "y" or userInput == "n"):
            x = 8675309 #because I can't use break statements apparently would normally just use while(True) for sub-loop and break here
    keepGoing = userInput == "y"