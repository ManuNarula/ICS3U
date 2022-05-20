##############################################
#Anotations:

# Name: Manu Narula 
# Date: April 12 2022
# PY4 - GUI Frontend 

##############################################
#Libaries: 
from tkinter import *

##############################################

NumberTheoryMain = Tk()
NumberTheoryMain.configure(bg="#232731")

valueX = StringVar()
valueY = StringVar()
objOutput = StringVar()
acceptableValue = StringVar()
permuationsOfXY = StringVar()
factorialOfX = StringVar()
factorialOfY = StringVar()
combinationsofXY = StringVar()
primeStats = StringVar()
gcdOfXY = StringVar()
lcmOfXY = StringVar()

##############################################
# Subprograms/Functions:
  
# Date: March 01
# Use PY2: The digits of a number to help you with this sub
# Input: Integer n 
# Output: The facotiral of a given integer 
def calcFactorial (n): # Note: Classic counting loop where it goes up by 1 until it reaches that number, all thoose numbers multiply by each other 
    factorial = 1 # Our float integer for this code 
    count = 1 # Start of with value 1 so we can increment this value 
    while count <= n: # Loops until count reaches the same value as n (the integer we passed through to this program)
        factorial = factorial * count # The main counting loop 
        count += 1 # Makes count (which starts from 1) slowly increment 
    return factorial # Returns the facotiral, which in the main program we print out 

# Purpose: To recall in the main to get the permuations of two set integer - For PY3
# Input: Integers entered/choosen by the user x 2 
# Output: Permuations of said integer 
# Date: March 01 2022
def caclPermuations (n,r): # Permuations, to caluclate it we require two integer, in this sub we label theese two integers "n" and "r", in the main
    if n <= r: # Since we can't rearange the equations (as it was already given to us by Mr.Smith) 
        temp = n # Stores the value of n as the variable temp, we do this so whatever changes we make to n does not affect the original value (so we can always recall it with minimal consequence)
        n = r # We now turn n to r 
        r = temp # And r to the orignal value of n 
    permutations = calcFactorial(n)/calcFactorial(n - r) # Formula to calculate the permuations - The placment of n and r matter in this equations, thats why we had to rearrange it 
    return permutations # Returns the permuations we calculated using the formula 

# Purpose: PY3 --> To get combinations, which we later print out in the main 
# Input: Two sets of integer 
# Output: The factorial of two given integer (Program crashes if no number is passed through)
# Date: March 02 2022
def calcCombinations (n, r): 
    if n <= r: 
        temp = n # Stores value of n inside temp
        n = r # Makes n have the value to r, we need this to arrange so that n > r 
        r = temp # Makes r into n 
    combinations = calcFactorial(n)/(calcFactorial(r) * calcFactorial(n-r)) # Formula to find the combinations 
    return combinations # Returns the value the program gets 

# Purpose: PY2 --> Calculate GCD which we recall in our main 
# Input: Two values 
# Output: Greetest common denominator between both integer
# Date: March 02 2022
def calcGCD (m,gcd): # Two given integers (our paramteres to this func)
    t = m % gcd # Formula to get gcd 
    if t > 0 or t < 0: # Re-arrange  
        m = gcd  
        gcd = t
        t = m % gcd
    return gcd # Returns the gcd we calulcated using the formula 

# Input: Two values 
# Output: Least common multiple between the two integers 
# Purpose: PY3 --> Find LCM, which we recall in the main 
# Date: March 03 2022
def calcLCM (m, n):
    lcm = m * n/calcGCD(m,n)
    return lcm

# Input: two integer 
# Output: The prime status, if it is prime we return it as "true" and if it is not prime we return it as "false"
# Purpose: PY3 --> Let the user know if it is prime, which we show in out main 
# Date: March 03 2022 
def isRelativelyPrime (x, y):
    if calcGCD(x,y) <= 1: 
        prime = "true"
    else: 
        prime = "false"
    return prime 

# Author: Manu Narula 
# Date: April 12 2022
# Parameters: N/A
# Input: N/A
# Returns: The Integer that was set through the text field 
# Purpose: Set The variables needed from the text field 
def AcceptValue():
    userInput1 = valueX.get()  
    userInput2 = valueY.get()
    low = 0
    high = 60  
    if (userInput1.isdigit() and userInput2.isdigit()):       
        validUserNumX = int(userInput1)
        validUserNumY = int(userInput2)
        if (validUserNumX < low or validUserNumX > high) or (validUserNumY < low or validUserNumY > high):
            strPS1 = "Your value must be lower then 60 and higher then 0 Try again:"
            acceptableValue.set(strPS1)
            factorialOfX.set("")
            factorialOfY.set("")
            permuationsOfXY.set("")
            combinationsofXY.set("")
            primeStats.set("")
            gcdOfXY.set("")
            lcmOfXY.set("")
        else:
            acceptableValue.set ("The value you entered was acceptable")

            # Re-calling sub's: 
            factorialReturnX = str(calcFactorial(validUserNumX))
            factorialReturnY = str(calcFactorial(validUserNumY))
            permReturn = str(caclPermuations(validUserNumX, validUserNumY))
            combReturn = str(calcCombinations(validUserNumX, validUserNumY))
            primeStatusReturn = str(isRelativelyPrime(validUserNumX, validUserNumY))
            gcdReturn = str(calcGCD(validUserNumX, validUserNumY))
            lcmReturn = str(calcLCM(validUserNumX, validUserNumY))

            # Displaying the results:
            statementOfFactorialX = "Factorial of x: " + factorialReturnX
            factorialOfX.set (statementOfFactorialX)
            statementOfFactorialY = "Factorial of y: " + factorialReturnY
            factorialOfY.set (statementOfFactorialY)
            statementOfPermuations = "Permuations: " + permReturn
            permuationsOfXY.set (statementOfPermuations)
            statementOfComb = "Combinations: " + combReturn
            combinationsofXY.set (statementOfComb)
            primeStatement = "Prime Status: " + primeStatusReturn
            primeStats.set (primeStatement)
            gcdStatment = "GCD: " + gcdReturn
            gcdOfXY.set (gcdStatment)
            lcmStatement = "LCM: " + lcmReturn
            lcmOfXY.set (lcmStatement)           
    else: 
        strPS1 = "Please enter integer's only"
        acceptableValue.set(strPS1)
        factorialOfX.set("")
        factorialOfY.set("")
        permuationsOfXY.set("")
        combinationsofXY.set("")
        primeStats.set("")
        gcdOfXY.set("")
        lcmOfXY.set("")

##############################################
# Creation of Window: 

# Widgets:
widLabelInteger1Name = Label(NumberTheoryMain,text="Inset X:",bg="#232731",fg="#81a2be")
widValueInteger1 = Entry(NumberTheoryMain, bd=4,bg="#FFFFFF",textvariable=valueX)
widLabelInteger2Name = Label(NumberTheoryMain,text="Insert Y:",bg="#232731",fg="#81a2be")
widValueInteger2 = Entry(NumberTheoryMain,bd=4,bg="#FFFFFF",textvariable=valueY)
widButtonClickedX = Button(NumberTheoryMain,text="Accept Values",bg="#81a2be",command=lambda:AcceptValue()) 
widTextFactorialStatementofX = Label(NumberTheoryMain,textvariable=factorialOfX,bg="#232731",fg="#81a2be")
widTextFactorialStatementofY = Label(NumberTheoryMain,textvariable=factorialOfY,bg="#232731",fg="#81a2be")
widTextCombStatement = Label(NumberTheoryMain,textvariable=combinationsofXY,bg="#232731",fg="#81a2be")
widTextPermStatement = Label(NumberTheoryMain,textvariable=permuationsOfXY ,bg="#232731",fg="#81a2be")
widTextGCDStatement = Label(NumberTheoryMain,textvariable=gcdOfXY,bg="#232731",fg="#81a2be")
widTextLCMStatement = Label(NumberTheoryMain,textvariable=lcmOfXY,bg="#232731",fg="#81a2be")
widTextPrimeStatement = Label(NumberTheoryMain,textvariable=primeStats,bg="#232731",fg="#81a2be")
acceptableValueStatement = Label(NumberTheoryMain, textvariable=acceptableValue,bg="#232731",fg="#81a2be")

# Positioning: 
widLabelInteger1Name.grid(row=2, column=2, padx=4)
widValueInteger1.grid (row=2, column=3)
widButtonClickedX.grid(row=3, column=4)
widLabelInteger2Name.grid(row=4, column=2)
widValueInteger2.grid(row=4,column=3)
acceptableValueStatement.grid(row=1,column=3)
widTextFactorialStatementofX.grid(row=5,column=3)
widTextFactorialStatementofY.grid(row=6,column=3)
widTextPermStatement.grid(row=7,column=3)
widTextCombStatement.grid(row=8,column=3)
widTextGCDStatement.grid(row=9,column=3)
widTextLCMStatement.grid(row=10,column=3)
widTextPrimeStatement.grid(row=11,column=3) 

##############################################

mainloop()
