# Author: Manu N 
# Date: Apr 29 2022
# Purpose: OOP -> Calendar Program for PY5

# Libaries:

# Subprograms:

# Classes:

# Author: Manu Narula
# Date: April 29 2022
# Purpose: Date Class --> The recipe for what a date is and how to display the calendar 
# Methods:
    # __int__
    # returnMonthName
    # returnLeapYear
    # returnMaxDay
    # calcZeller
    # returnDayName
    # calcValid
    # getDate
    # __str__
    # displayCalendar
# Dependencies:
    # None --> getPositiveInteger already included in Date class
class Date:
    # Author: Manu Narula
    # Date: April 29 2022
    # Input: value of day, month, and year --> as integers
    # Output: N/A
    # Purpose: definitions for what a day, month, and year is --> all as integers
    def __init__(self, day = 1, month = 1, year = 2019):
        self.day = day
        self.month = month
        self.year = year   

    # Author: Manu Narula
    # Date: April 29 2022
    # Input: month --> self.month
    # Output: The name of the month --> in string format
    # Purpose: to return the name of the month so we can display to the user in displayCalendar sub
    def returnMonthName(self) :
        if self.month == 1:
            monthClassification = "January"
        elif self.month == 2:
            monthClassification = "Febuary"
        elif self.month == 3:
            monthClassification = "March"
        elif self.month == 4: 
            monthClassification = "April"
        elif self.month == 5: 
            monthClassification = "May" # The best month
        elif self.month == 6: 
            monthClassification = "June"
        elif self.month == 7: 
            monthClassification = "July"
        elif self.month == 8: 
            monthClassification = "August"
        elif self.month == 9: 
            monthClassification = "September"
        elif self.month == 10:
            monthClassification = "October"
        elif self.month == 11:
            monthClassification = "November"
        elif self.month == 12: 
            monthClassification = "December"
        return monthClassification

    # Author: Manu N
    # Date: April 29 2022
    # Input: Year --> self.year
    # Output: Boolean status if its a prime year or not
    # Purpose: To return if the year is a leap year --> so we can calculate the number of day's in a month
    def returnLeapYear(self): 
        if (self.year % 100) == 0: # Determines if its a centurary year
            if (self.year % 400 ) == 0:
                leapYearStatus = True
            else: 
                leapYearStatus = False
        elif (self.year % 4) == 0:
            leapYearStatus = True
        else:
            leapYearStatus = False
        return leapYearStatus 

    # Author: Manu N
    # Date: May 2 2022
    # Input: Month --> self.month
    # Output: The maxium number of days in that month
    # Purpose: To display the number of days inside the calendar
    def returnMaxDay(self):
        if self.month == 1 or self.month == 3 or self.month == 5 or self.month == 7 or self.month == 8 or self.month == 10 or self.month == 12:
            maxDayCount = 31
        elif self.month == 4 or self.month == 6 or self.month == 9 or self.month == 11:
            maxDayCount = 30 
        else:
            maxDayCount = 28
            if self.returnLeapYear() == True:
                maxDayCount = 29
        if self.returnLeapYear() == True:
                maxDayCount = 29 
        return maxDayCount

    # Author: Manu N
    # Date: April 30 2022
    # Input: month, year, and date
    # Output: The day of the month
    # Purpose: Using the Zeller formula to determine what day the month starts on 
    def calcZeller(self):
        intM = self.month - 2
        intYear = self.year
        if intM <= 0:
            intM = intM + 12
            intYear = intYear - 1
        intP = intYear // 100
        intR = intYear % 100   
        return ((self.day + (26 * intM - 2) // 10 + intR + intR // 4 + intP // 4 + 5 * intP) % 7 )
    
    # Author: Manu N
    # Date: April 29 2022
    # Input: The result of zeller
    # Output: The name of the date
    # Purpose: Using the zeller formula to find the date, return the name of the day --> so we can print it out in string format mm/dd/yy
    def returnDayName(self): 
        intZellerResults = self.calcZeller()
        if intZellerResults == 0:
            strDateName = "Sunday"
        elif intZellerResults == 1:
            strDateName = "Monday"
        elif intZellerResults == 2:
            strDateName = "Tuesday"
        elif intZellerResults == 3: 
            strDateName = "Wednesday"
        elif intZellerResults == 4:
            strDateName = "Thursday"
        elif intZellerResults == 5: 
            strDateName = "Friday"
        #elif intZellerResults == 7:
            #strDateName = "Sunday"
        else:
            strDateName = "Saturday"
        return strDateName  


    # Author: Manu N
    # Date: May 4 2022
    # Input: True/False indicating if its a leap year or not
    # Output: Status of the boolean 
    def calcValid (self):
        leapYearStatus = self.returnLeapYear(self)
        if (self.day >= 1) and (self.day < Date.returnMaxDay(self, leapYearStatus)):
            boolValidStatus = True
        elif (self.month >= 1) and (self.month <= 12):
            boolValidStatus = True
        else:
            boolValidStatus = False
        return boolValidStatus

    # Input: User enters a positive integer 
    # Purpose: Checking to see the number the user inputed is correct (not a string, not a negative int, not a number that doesn't fit the boundaryt ) - PY2
    # Source: October 12, 2022 Mr.Smith sanbox 
    def getPositiveInteger (self,low = 0, high=60, prompt = "Enter a positive integer "): # We set our boundaries over here, and make 0 the absolute lowest, and 60 the absoulte highest 
        validNum = low - 1 # Float integer 
        while validNum < low or validNum > high: # Loop that keeps repeating until the user enters a valid positive integer 
            newprompt = prompt + "which is between " + str(low) + " and " + str(high) + " : " # Nicely formatted feedback 
            strValidNum = input(newprompt) 
            validNum = int(strValidNum)
        validNum = int(strValidNum)
        return validNum # It returns the valid number to the main program. All the other subs refrence this valid number to use, to get the values they need

    # Author: Manu N
    # Date: May 4 2022
    # Input: User inputs the month/year they would like to use
    # Output: None
    # Parameters: Self, getPositiveInteger
    # Purpose: To let the choose the dates he would like while bob proofing it 
    def getDate (self):
        userIntYear = self.getPositiveInteger (prompt="Enter a valid year: ", low=1500, high=2200) 
        userIntMonth = self.getPositiveInteger (prompt="Enter a valid month: ", low = 1, high = 12)
        self.year = userIntYear
        self.month = userIntMonth
        maxiumDay = int(self.returnMaxDay())
        userIntDay = self.getPositiveInteger (prompt="Enter a valid day: ", low=0, high=maxiumDay)
        self.day = userIntDay
        

    # Author: Manu N
    # Date: May 4 2022
    # Input: N/A
    # Output: The Date wrutten in string format
    # Parameters: self
    # Purpose: To display the user the date in easy human readable format 
    def __str__(self):
        strDate = self.returnDayName()  
        strDateNum = str(self.day)
        strMonth = self.returnMonthName()  
        strYear = str(self.year)
        strDateFormat = strDate + ", " + strMonth + " " + strDateNum + ", " + strYear
        return strDateFormat

   # Author: Manu N
   # Date: May 6 2022
   # Input: Date, Month, Year, LeapYearStatus, string format
   # Output: Nicely printed calendar
   # Parameters: Self
   # Purpose: Display a nicely printed calendar to the user
    def displayCalendar (self): 
        date = 1 
        intDateWeek = 1
        print("")
        strDisplay = self.__str__()
        print ("",strDisplay)
        print ("Sun Mon Tue Wed Thu Fri Sat")       
        startDay = Date(1, self.month, self.year)
        dateStartSpacing = startDay.calcZeller()
        for x in range (dateStartSpacing):
        #    print ("  ", end="")
            print ("", end=" ")
        for x in range (self.returnMaxDay()):  
            print (" ", "%2.0i" % date, end="")
            #if date > 10:
            #    print (" ",date,end=" ")
            #else:
            #    print (" ",date,end="")
            date += 1
            intDateWeek += 1
            if intDateWeek > 7:
                print("\n")
                intDateWeek = 1 

    # Author: Manu N 
    # Date: May 20 2022 
    # Input: date, month, year, zeller results, leapyear results 
    # Output: Show case calendar information
    # Parameters: self 
    # Purpose: To test out all of my subprograms that I am going to be feeding into the calendar to avoid errors 
    def testingCalendar(self):
        startDay = Date(1, self.month, self.year)
        startDayZeller = startDay.calcZeller()
        print("The starting day:",startDay,)  
        print("The calcZeller Results: ",startDayZeller,)  
        leapsYearDates = self.returnLeapYear()
        print ("Leap year status:",leapsYearDates,)        

     
#Main:
myDate = Date()
reRunStatus = "y"
while reRunStatus == "y":
    myDate.getDate()
    myDate.displayCalendar()
#    myDate.testingCalendar()
    print ("")
    reRunStatus = input("Will you like to rerun the program(y/n): ")

if reRunStatus != "y":
    print ("Bye, Have a great day!")
