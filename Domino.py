
# Author: Manu N
# Date: May 11 2022
# Task: PY5 --> OOP1 Domino Class

# Libaries:
import random
from tkinter import * 

# Initalizing Tkinter:
DominoBoard = Tk()
DominoBoard.resizable(0,0)
DominoBoard.config(bg="#FFFFFF")

# Classes:

# Author: Manu N
# Date: May 11 2022
# Purpose: Domino class which we will later use comisiton of classes to make better
# Methods:
# Dependencies: 
    # tkinter 
    # random
class Domino:
    # Author: Manu N
    # Date: May 11 2022
    # Purpose: Defining the integers that will make a domino
    # Parameters: self, value=0, size=60, orientation="H"
    # Input: a domino value, size of the domino, and its orientation 
    # Output: N/A
    # Source: Mr.Smith PY5SandboxQ2 (file on Google Classroom) 
    def __init__(self, value=1, size=60, orientation = "H"):        
        if str(value).isdigit():
                    value = int(value)
                    if value >= 0 and value <= 66 and value%10 <= 6:
                        self.value = value
                    else:
                        self.value = 0
        else:
                self.value = 0

        if str(size).isdigit():
                    size = int(size)
                    if size >= 30 and size <= 100:
                        self.size = size
                    else:
                        self.size = 60
        else:
            self.size = 60                   
        if str(orientation) == "H" or str(orientation) == "V":
            self.orientation = str(orientation)
        else:
            self.orientation = "H"

        self.diameter = self.size // 5
        self.gap = self.diameter // 2
            
    # Author: Manu N
    # Date: May 11 2022
    # Purpose: Return domino value as string
    # Parameters: self
    # Input: value of the domino
    # Output: N/A
    # Return: A string showing the value and orientation of domino
    def ___str__ (self):
        dominoValueStr = "Value:" + (str(self.value)) + "Orientation:" + (str(self.orientation)) + "Size:" + (str(self.value)) 
        return dominoValueStr

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


    # Author: Manu N
    # Date: May 11 2022
    # Purpose: To get a proper value from the user for the GUI program 
    # Input: User inputs a valid value for the domino
    # Output: N/A
    # Return: N/A
    # Parameters: self        
    def getValue(self):
        userValue = self.positiveInteger(low=0, high=66, prompt="Please enter the value for the domino you would like to use")

    # Author: Manu N
    # Date: May 12 2022
    # Purpose: To set the value the user entered into a valid number - While bob proofing it
    # Parameters: self.value
    # Input: The value user entered from getValue
    # Output: Valid number set for self.value
    # Return: N/A
    def setValue (self, anotherValue):
        if (anotherValue.isdigit()):
            aNewDigitValue = int(anotherValue)
            if aNewDigitValue >= 0 and aNewDigitValue <= 66:
                self.value = storedIntValue
            else:
                self.value = 0
        else:
            self.value = 0 
                                         
    # Author: Manu N
    # Date: May 13 2022
    # Purpose: To flip the value 
    # Parameters: self 
    # Input: value
    # Output: fliped value 
    # Return: the Flipped number --> That we calculated 
    def flip(self):
        if self.value >= 10:
            intTensDigit = self.value // 10
        else:
            intTensDigit = 0
        intOnesDigit = self.value - intTensDigit
        intOnesDigit = self.value * 10
        intFlipedValue = intOnesDigit + intTensDigit
        return intFlipedValue 

    # Author: Manu Narula 
    # Date: May 17 2022
    # Purpose: Set the orientation value (flipped)
    # Parameters: self
    # Input: Orientation 
    # Output: Flipped Version of the orientation
    # Return: N/A
    def setOrientation (self):
        if self.orientation == "H": 
            self.orientation = "V"
        else: 
            self.orientation = "H"
            
    # Author: Manu N 
    # Date: May 17 2022 
    # Purpose: Set the size 
    # Parameters: self, domino size (determined by the user)
    # Input: the size a user selected
    # Output: N/A
    # Return: N/A
    def setSize(self, intUserSize): 
        if intUserSize >= 30 and intUserSize <= 100:
            self.size = intUserSize
        else: 
            self.size = 60 # We keep the default unless the user sets it to a different range
        self.diameter = self.size // 5
        self.gap = self.diameter // 2
        #x = self.size 
        #y = self.size * 2

    # Author: Manu N 
    # Date: May 17 2022
    # Purpose: To randomize domino values
    # Parameters: self
    # Inpout: N/A
    # Output: N/A
    # Return: N/A
    def randomize(self): 
       generatedIntValue = random.randint(1, 6)* 10 + random.randint(1,6) # For the domino faces to work the first face has to be in the range from 1 to 6 and the second face has to be from 1 to 6
       self.value = int(generatedIntValue)

    # Author: Manu N 
    # Date: May 17 2022
    # Purpose: 
    # Parameters: 
    # Input: 
    # Output:
    # Return:
#    def drawHalf(self, canvas, x=0, y=0, value=0 ):
#        canvas.create_rectangle(x,y,x+self.size,y+self.size)

    # Author: Manu N 
    # Date: May 17 2022
    # Purpose: Two part program paired with the drawhalf to draw dominos --> Draw handles the sizing and orientation
    # Parameters: self, canvas, x-coordinate (inside canvas), y-coordinate inside canvas
    # Input: N/A
    # Output: N/A
    # Return: N/A
    def draw(self,canvas,x,y):        
        if self.orientation == "H" or self.orientation == "h":
            self.drawHalf(canvas, x, y, self.value//10)
            self.drawHalf(canvas, x+self.size,y,self.value%10)

        elif self.orientation == "V" or self.orientation == "v": 
            self.drawHalf(canvas, x, y,self.value//10)
            self.drawHalf(canvas, x,y+self.size, self.value%10)
            

    # Author: Manu N 
    # Date: May 18 2022
    # Purpose: Two part program paired with draw to create dominos --> Drawhalf handles the dot placement and the dominio body
    # Parameters: self, canvas, x-coordinate(inside canvas), y-coordinate(inside canvas), domino values
    # Input: value, x coord (in canvas), and y coordinate (in canvas)
    # Output: A perfectly crafted dominos
    # Return: N/A
    def drawHalf(self,c, x, y, value):
        c.create_rectangle(x,y, x + self.size, y + self.size, width = 1, outline="white", fill="#000000")        
        if value == 1:
            c.create_rectangle(x,y, x + self.size, y + self.size, width = 1, outline="white", fill="#000000")    
            c.create_oval(x + self.gap*2+self.diameter, y + self.gap*2+self.diameter, x + self.gap*2 + self.diameter*2, y + self.gap*2 + self.diameter*2, fill="#FFFFFF") 
        if value == 2:     
            c.create_oval(x + self.gap, y + self.gap, x + self.gap + self.diameter, y + self.gap + self.diameter, fill="#FFFFFF")
            c.create_oval(x + self.gap*3+self.diameter*2, y + self.gap*3 + self.diameter*2, x + self.gap*3 + self.diameter*3, y + self.gap*3 + self.diameter*3, fill="#FFFFFF")
        if value == 3:
            c.create_oval(x + self.gap*2+self.diameter, y + self.gap*2+self.diameter, x + self.gap*2 + self.diameter*2, y + self.gap*2 + self.diameter*2, fill="#FFFFFF") 
            c.create_oval(x + self.gap, y + self.gap, x + self.gap + self.diameter, y + self.gap + self.diameter, fill="#FFFFFF")
            c.create_oval(x + self.gap*3+self.diameter*2, y + self.gap*3 + self.diameter*2, x + self.gap*3 + self.diameter*3, y + self.gap*3 + self.diameter*3, fill="#FFFFFF")
        if value == 4:
            c.create_oval(x + self.gap, y + self.gap, x + self.gap + self.diameter, y + self.gap + self.diameter, fill="#FFFFFF")
            c.create_oval(x + self.gap*3+self.diameter*3, y + self.gap, x + self.gap + self.diameter*3, y + self.gap + self.diameter, fill="#FFFFFF")
            c.create_oval(x + self.gap*3+self.diameter*2, y + self.gap*3 + self.diameter*2, x + self.gap*3 + self.diameter*3, y + self.gap*3 + self.diameter*3, fill="#FFFFFF")
            c.create_oval(x + self.gap, y + self.gap*3 + self.diameter*2, x + self.gap + self.diameter, y + self.gap*3 + self.diameter*3, fill="#FFFFFF")
        if value == 5:
            c.create_oval(x + self.gap, y + self.gap, x + self.gap + self.diameter, y + self.gap + self.diameter, fill="#FFFFFF")
            c.create_oval(x + self.gap*3+self.diameter*3, y + self.gap, x + self.gap + self.diameter*3, y + self.gap + self.diameter, fill="#FFFFFF")
            c.create_oval(x + self.gap*3+self.diameter*2, y + self.gap*3 + self.diameter*2, x + self.gap*3 + self.diameter*3, y + self.gap*3 + self.diameter*3, fill="#FFFFFF")
            c.create_oval(x + self.gap, y + self.gap*3 + self.diameter*2, x + self.gap + self.diameter, y + self.gap*3 + self.diameter*3, fill="#FFFFFF")
            c.create_oval(x + self.gap*2+self.diameter, y + self.gap*2+self.diameter, x + self.gap*2 + self.diameter*2, y + self.gap*2 + self.diameter*2, fill="#FFFFFF")
        if value == 6:
            c.create_oval(x + self.gap, y + self.gap, x + self.gap + self.diameter, y + self.gap + self.diameter, fill="#FFFFFF")
            c.create_oval(x + self.gap*3+self.diameter*3, y + self.gap, x + self.gap + self.diameter*3, y + self.gap + self.diameter, fill="#FFFFFF")
            c.create_oval(x + self.gap*3+self.diameter*3, y + self.gap*2 + self.diameter, x + self.gap + self.diameter*3, y + self.gap*2 + self.diameter*2, fill="#FFFFFF")
            c.create_oval(x + self.gap, y + self.gap*2 + self.diameter, x + self.gap + self.diameter, y + self.gap*2 + self.diameter*2, fill="#FFFFFF")
            c.create_oval(x + self.gap*3+self.diameter*2, y + self.gap*3 + self.diameter*2, x + self.gap*3 + self.diameter*3, y + self.gap*3 + self.diameter*3, fill="#FFFFFF")
            c.create_oval(x + self.gap, y + self.gap*3 + self.diameter*2, x + self.gap + self.diameter, y + self.gap*3 + self.diameter*3, fill="#FFFFFF")

                              
# Subprograms:

# Author: Manu N
# Source: Mr.Smith Sandbox
# Input: The keypress
# Output: N/A
# Return: N/A
# Parameters: Event
def keyPressed(event):  
    global xHolder
    myDomino = Domino()
    myDomino.randomize()
    myDomino.setSize(90)
    if event.char == "h" or event.char == "H":
        print ("Horizontal")
        myDomino.orientation = "H"
        myDomino.draw(canvas, xHolder, 25)
        xHolder += 200 + 25
    elif event.char == "r" or event.char == "R": # randomly chooses an orientation   
        randomGenerate = random.randint (1,2)
        if randomGenerate == 1:
            myDomino.orientation = "V"
            print ("random: vertical")
        else:
            myDomino.orientation = "H"
            print("random: horizontal")
        myDomino.draw(canvas,xHolder,25)
        xHolder += 200 + 25
    elif event.char == "v" or event.char == "V":
        print ("Vertical")
        myDomino.orientation = "V"
        myDomino.draw(canvas,xHolder, 25)
        xHolder += 200 + 25
    else: 
        # Do nothing 
        print ("Wrong Input, use v,h, or r")



# Author: Manu N
# Date: May 31 2022
# Purpose:
# Input:
# Output:
# Parameters:
##def newLineMechanics(numOfDominos):
##    while numOfDominos % 4 == 0: # Once there are 4 dominos (the max limit this canvas can support)
##        canvas.delete("all") # It will use the canvas tool to delete them on so we can place the dominos again
##    numOfDominos == 0 # Then we restart the domino number of domino counter 

############### main program
xHolder = 25
myDomino = Domino()
canvas = Canvas(DominoBoard, width=900, height=300)
canvas.config(background="#FFFFFF")
canvas.bind("<Key>",keyPressed)
canvas.pack()
canvas.focus_set()

mainloop()

