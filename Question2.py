class clockTime:

    # Constructor that initializes attributes to 0
    def __init__(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

    # Asks user for the no. of hours, checks if no. of hours is 0 - 23, sets the hours attribute
    def setHours(self):
        self.hours = int(input("Key in the number of hours from 0 - 23: "))
        
        #User re-enters hours if hours is out of range
        while (self.hours < 0 or self.hours > 23):
            print("Invalid input! Hours only from 0 to 23.")
            self.hours = int(input("Key in the number of hours from 0 - 23: "))


    #Asks user for the no. of minutes, checks if no. of minutes is 0 - 59, sets the minutes attribute
    def setMinutes(self):
        self.minutes = int(input("Key in the number of minutes from 0 -  59: "))
        
        #User re-enters if minutes is out of range
        while (self.minutes < 0 or self.minutes > 59):
            print("Invalid input! Minutes only from 0 to 59.")
            self.minutes = int(input("Key in the number of minutes from 0 -  59: "))


    #Asks user for the no. of seconds, checks if no. of seconds is 0 - 59, sets the seconds attribute
    def setSeconds(self):
        self.seconds = int(input("Key in the number of seconds from 0 -  59: "))
        
        #User re-enters if seconds is out of range
        while (self.seconds < 0 or self.seconds > 59):
            print("Invalid input! Seconds only from 0 to 59.")
            self.seconds = int(input("Key in the number of seconds from 0 -  59: "))


    #Calling Functions
    def setTime(self):
        self.setHours()
        self.setMinutes()
        self.setSeconds()

    #Prints time in the following format
    def showTime(self):
        print("The current time is: {:02d}:{:02d}:{:02d}".format(self.hours, self.minutes, self.seconds))

# Creates clockTime object
currentTime = clockTime()
# Sets the time
currentTime.setTime()
# Prints the time
currentTime.showTime()