#Name: Manu N
#Date: June 10 2022
#Purpose:

##########################################

# Libaries:
import random

##########################################
# Classes: 
 
#Author: Manu N
#Date:June 10 2022
#Purpose: Different methods developed on how to handle a array (without crashing)
#Methods:
#    - __init__
#    - __str__
#    - initAsNum 
#    - initAsSeq
#    - calcTotal
#    - calcMean
#    - findLargest
#    - calcFreq
#    - insertAt
#    - removeAt
#    - removeAll
#    - findFirst
#    - isSorted
#Depedencies:
#    - none
class IntGroup:
    #Author: Manu J 
    #Date: June 10 2022
    #Purpose: constructor - initalizes all of the main varriable and set up the class enviornment
    #Input: a size
    #Output: A randomized array
    #Parameters: self, and size
    #Return: N/A    
    def __init__ (self, size=0):
        if size > 0 and size <= 20:
            self.size = size
            self.crashStatus = False #Instead of type checking in each subprogram if the array has value we can just create a class dependant varriable
            # that initalizes each time we add a value. So incase if the array has no value and will crash we can enclose the array in a if statement that checks for this status 
        elif size == 0:
            self.size = 0
            self.crashStatus = True 
        else:
            self.size = 0
            self.crashStatus = True #   
        self.size = size 
        self.partitions = []
        for count in range(size):# fills the string up with random integers
            getIntNumbers = random.randint(1, size)
            self.partitions.append(int(getIntNumbers))

    #Author: Manu N
    #Date: June 10 2022
    #Purpose: Print intGroup in a format that showcases the size and all of its value in array 
    #Input: The array
    #Output: Nicely printed format
    #Parameters: self
    #Return: String which we print out     
    def __str__(self):
        return (str(self.partitions)+ " " + "size: " + str(len(self.partitions)))

    #Author: Manu N
    #Date: June 10 2022
    #Purpose: Recreate the list with a new two integers stored inside 
    #Input: Value 1 to fill array, Value 2 to fill array
    #Output: N/A
    #Parameters: sef, first value, second value 
    #Returns: N/A
    def initAsNum(self,size=2,value=0):
        self.partitions = []
        size = str(size)
        value = str(value)
        count = 0
        if size.isdigit() and value.isdigit():
            size = int(size)
            if size >= 0 and size <= 20:
                while count != size: 
                    self.partitions.append(value)
                    count += 1
                
    #Author: Manu N
    #Date: June 10 2022
    #Purpose: Recreates the list with incrementing values until reaching the size 
    #Input: size to go up to 
    #Output: N/A
    #Parmaters: self, value
    #Returns: N/A
    def initAsSeq(self, numericalIntValue):
        numericalIntValue = str(numericalIntValue)
        if numericalIntValue.isdigit():
            self.partitions = []
            numericalIntValue = int(numericalIntValue)
            count = 0
            while count != numericalIntValue:
                count += 1 # We do count before this task since on the example it starts from 1
                self.partitions.append(count)
            self.crashStatus = False 

    #Author: Manu N
    #Date: June 11 2022 
    #Purpose: To calculate total of all integers in array
    #Input: Values in array
    #Output: Total sum
    #Parameters: self
    #Returns: Total 
    def calcTotal(self):
        self.total = 0
        integersInArray = 0
        for integersInArray in self.partitions:
            self.total = self.total + integersInArray
        return self.total  

    #Author: Manu N 
    #Date: June 11 2022
    #Purpose: to get the average of integers in array
    #Input: Array 
    #Output: Average percantage 
    #Parameters: self
    #Returns: Mean 
    def calcMean(self): 
        self.total = 0
        for integersInArray in self.partitions:
            self.total = self.total + integersInArray
        self.mean = self.total / len(self.partitions)
        return (str(round(self.mean, 1)) + "%")
        
    #Author: Manu N
    #Date: June 11 2022
    #Purpose: find largest value inside the string 
    #Input: N/A
    #Output: Largest largest integer inside array 
    #Parameters: N/A
    #Returns Largest integer 
    def findLargest(self):
        if self.crashStatus == False:
            self.largestInt = max(self.partitions)
        else:
            self.largestInt = 0
        return self.largestInt

    # Author: Manu N 
    # Date: June 11 2022
    # Purpose: Find how much times an integer is repeated in array
    # Input: A value to locate
    # Output: Number of times its repeated
    # Parameters: Self, and value 
    # Return: Number of times the value is shown in array
    def calcFreq(self, aElement):
        aElement = str(aElement)
        if aElement.isdigit():
            aElement = int(aElement)
            if aElement in self.partitions:
                self.frequencyOfInt = self.partitions.count(aElement)
            else: 
                self.frequencyOfInt = 0
        else: 
            self.frequencyOfInt = 0
        return self.frequencyOfInt

    #Author: Manu N
    #Date: June 11 2022
    #Purpose: To insdert a value inside a position user choose for the string 
    #Input: position, value 
    #Output: A new string with the value user choose in the position user choose 
    #Parameters: self, the position, the value 
    #Returns: N/A
    def insertAt(self,position, value):
        position = str(position)
        value = str(value)
        if position.isdigit and value.isdigit():
            position = int(position)
            value = int(value)
            if position < 0:
                position = 0
            if position > len(self.partitions): # see's if the position user requested is at the end of the string 
                position = int(len(self.partitions)) 
            self.partitions.insert(position,value)
            self.crashStatus = False # since we are inserting a value that means we have an integer in their 

    #Author: Manu N
    #Date: June 11 2022
    #Purpose: To remove a value at a specific position in array 
    #Input: position
    #Output: A new array with the value in selected position removed 
    #Parameters: self, and position
    #Returns: N/A
    def removeAt(self,position=0):
        if position <= len(self.partitions) and position >= 0:
            if self.crashStatus == False:
                self.partitions.pop(position)

    #Author:Manu N
    #Date: June 11 2022
    #Purpose: Remove all value inside an array
    #Input: the value you would like to wipe inside array 
    #Output: String without that value ever existing 
    #Parameters: self, the value 
    #Returns: N/A
    def removeAll(self, value):
        count = 0
        value = str(value)
        if value.isdigit():
            value = int(value)
            #for intNum in self.partitions:
            #    if intNum == value:
            #        tempValueCount = self.partitions.count(value)
            #        valueInArray = True
            #    else:
            #        valueInArray = False
            #if valueInArray == True:
            #    while count != tempValueCount:
            #        self.partitions.remove(value)
            #        count += 1
            if value in self.partitions:
                tempValueCount = self.partitions.count(value)
                while count != tempValueCount:
                    self.partitions.remove(value)
                    count += 1
                    #    self.partitions.remove(value)

    #Author: Manu N
    #Date: June 11 2022
    #Purpose:
    #Input:
    #Output:
    #Parameters:
    #Returns:
    def findFirst(self, valueToFind): 
        #calcForCount = 0
        valueToFind = str(valueToFind)
        if valueToFind.isdigit():
            valueToFind = int(valueToFind)
#            for numericalValue in self.partitions:
#                if numericalValue == valueToFind:
#                    valueInArray = True 
#            if valueInArray == True:
#                self.returnPosition = self.partitions.index(valueToFind, 0) + 1 # We add one because list starts from 0 
#            else:
#                self.returnPosition = - 1
            if valueToFind in self.partitions:
                self.returnPosition = self.partitions.index(valueToFind, 0) + 1 
            else:
                self.returnPosition = -1
        else:
            self.returnPosition = -1
        return self.returnPosition

    #Author: Manu N
    #Date: June 11 2022
    #Purpose: To check is the list is sorted
    #Input: Array
    #Output: Boolean status for sorted array
    #Parameters: self
    #Returns: Boolean status showcasing if its sorted or not 
##    def isSorted(self):
##        sortedList = self.partitions.sort()
##        for intNumbers in self.partitions:
##            
       

# Input: User enters a positive integer 
# Purpose: Checking to see the number the user inputed is correct (not a string, not a negative int, not a number that doesn't fit the boundaryt ) - PY2
# Source: October 12, 2022 Mr.Smith sanbox 
def getPositiveInteger (low = 0, high = 60, prompt = "Enter a positive integer "): # We set our boundaries over here, and make 0 the absolute lowest, and 60 the absoulte highest 
    validNum = low - 1 # Float integer 
    while validNum < low or validNum > high: # Loop that keeps repeating until the user enters a valid positive integer 
        newprompt = prompt + "which is between " + str(low) + " and " + str(high) + " : " # Nicely formatted feedback 
        strValidNum = input(newprompt) 
        validNum = int(strValidNum)
    validNum = int(strValidNum)
    return validNum # It returns the valid number to the main program. All the other subs refrence this valid number to use, to get the values they need

      
##############
# Main: 

rerunStatus = "y"
while rerunStatus == "y":
    arraySize = getPositiveInteger(low=0, high=20, prompt="Please select your array size ")
    myInt = IntGroup(arraySize)
    print("Your array is:")
    print(myInt)
    print("Avaialable options:", "1) Add values to array", "2) Get total", "3) Recreate the list", \
          "4) get Mean of array" , "5) Get the largest value of array", \
          "6) Find integers", "7) Remove values from your array", sep="\n")
    userSel = getPositiveInteger(prompt="From the menu choose a option ", low=1, high=7)
    if userSel == 1:
        intUserValue = getPositiveInteger(prompt = "Enter a value you would like to use ", low=0, high=20)
        intUserPosition = getPositiveInteger(prompt="Enter a position you would like to use ", low=0, high = arraySize)             
        IntGroup.insertAt(myInt,position=intUserPosition, value=intUserValue)
        print(myInt)
    elif userSel == 2:
        print("Your total:",IntGroup.calcTotal(myInt))
    elif userSel == 3:
        print("1) recreate the list with value and size", "2) recreate the list with to parameter", sep="\n")
        menuSel = getPositiveInteger(prompt="Enter a option ", low=1, high=2)
        if menuSel == 1:
            intUserSize = getPositiveInteger(prompt="Enter a size ", low=0, high= 20)
            intUserValue = getPositiveInteger(prompt="Enter a value ", low=0, high=intUserSize)
            IntGroup.initAsNum(myInt,size=intUserSize, value=intUserValue) # got to fix it for only size and a value
            print(myInt)
        else:
            intUserSize = getPositiveInteger(prompt="Please enter a size ", low=0, high=20)
            IntGroup.initAsSeq(myInt, numericalIntValue=intUserSize)
            print(myInt)
    elif userSel == 4:
        print("The mean is:",IntGroup.calcMean(myInt))
    elif userSel == 5:
        print("The largest:",IntGroup.findLargest(myInt))
    elif userSel == 6:
        print("1) Find how many element in one array", "2) Find position of a value in array", sep="\n")
        menuSel= getPositiveInteger(prompt="Select one option ", low=1, high=2)
        intUserValue = getPositiveInteger(prompt="Enter a value",low=0, high=IntGroup.findLargest(myInt))
        if menuSel == 1:
            print("Count of a value in array is: ",IntGroup.calcFreq(myInt,aElement=intUserValue))
        else:
            print("Position of value:",intUserValue," is",IntGroup.findFirst(myInt, valueToFind=intUserValue))
    else: 
        print("1) Remove a value at the position", "2) Remove all use of an integer", sep="\n")
        menuSel = getPositiveInteger(prompt="Please select one of theese values ", high=2, low=0)
        if menuSel == 1: 
            intUserPosition = getPositiveInteger(prompt="Please enter the position", low=0, high=arraySize)
            IntGroup.removeAt(myInt,position=intUserPosition)
            print(myInt)
        else:
            intUserValue = getPositiveInteger(prompt="Please enter a value you would like to erase from array ", low=0, high=IntGroup.findLargest(myInt))
            IntGroup.removeAll(myInt,value=intUserValue)
            print(myInt)
        rerunStatus = input("Would you like to rerun this program(y/n)")