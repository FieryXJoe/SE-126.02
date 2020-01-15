#Joseph Sherry
#Lab 1A
############################
#keepGoing          boolean loop vatiable
#maxCapacity        maximum room capacity based on user input
#plannedAttendance  planned attendees based on user input

keepGoing = True
while (keepGoing):
    maxCapacity = int(input("Enter the maximum capacity of the room: "))
    plannedAttedance = int(input("How many people want to attend the event?: "))
    if(maxCapacity >= plannedAttedance):
        print("Legally ", (maxCapacity - plannedAttedance), " more people may attend your event")
    else:
        print("Legally ", (plannedAttedance - maxCapacity), " people must be uninvited from your event")
    keepGoing = input("Do you have more data to input (y/n)?").lower() == "y"