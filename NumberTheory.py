# Author: Manu N
# Date: March 21 2022 
# PY3 - The Number Theory
# Purpose: Returning Permuations, Combinations, Factorial, LCM, and GCD of the integer. 

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

#____________________________________________________________________________________________________________________________________________________

# Main program 
# Date: March 03 2022 

# Use of Get Positive Integer sub, to let the user input a number, we take the integer the user selected and type check it to make sure it fits the boundaries of the function "getPositiveInteger". We take this integer and store it inside UserInputValue varriable 
userInputValue1 = getPositiveInteger()
userInputValue2 = getPositiveInteger(prompt="Second ")

# Finds the Factorial of the integer 
factorialofValue1 = calcFactorial(userInputValue1)
factorialofValue2 = calcFactorial(userInputValue2)

# Finds the permutation of the number 
permutationofValue = caclPermuations(userInputValue1, userInputValue2)

# Finds the combination of the number 
combinationsofValue = calcCombinations(userInputValue1, userInputValue2)

# Finding the gcm and lcm of Integer 1 and Integer 2 
gcdOfValues = calcGCD(userInputValue1, userInputValue2) 
lcmofValues = calcLCM(userInputValue1, userInputValue2)

# Finds if the number are prime or not 
isPrime = isRelativelyPrime(userInputValue1, userInputValue2)

# Prints all of the results we got from our code, in a visually appealing way for the user who ran this program to see 
print("Values given:",userInputValue1,",",userInputValue2,)
print("Factorial:",factorialofValue1,",",factorialofValue2,)
print("Permuations:",permutationofValue,"")
print("Combinations:",combinationsofValue,"")
print("GCD:",gcdOfValues,"")
print ("LCM:",lcmofValues,"")
print ("Prime Status:",isPrime,"")

print ("")
rerun = input("Would you like to rerun this program?(y/n)") # Reruns this program 
while rerun == 'y':
    print ("Restarting!")
    userInputValue1 = getPositiveInteger()
    userInputValue2 = getPositiveInteger(prompt="Second")
    factorialofValue1 = calcFactorial(userInputValue1)
    factorialofValue2 = calcFactorial(userInputValue2)
    permutationofValue = caclPermuations(userInputValue1, userInputValue2)
    combinationsofValue = calcCombinations(userInputValue1, userInputValue2)
    gcdOfValues = calcGCD(userInputValue1, userInputValue2) 
    lcmofValues = calcLCM(userInputValue1, userInputValue2)
    isPrime = isRelativelyPrime(userInputValue1, userInputValue2)
    print("Values given:",userInputValue1,",",userInputValue2,)
    print("Factorial:",factorialofValue1,",",factorialofValue2,)
    print("Permuations:",permutationofValue,"")
    print("Combinations:",combinationsofValue,"")
    print("GCD:",gcdOfValues,"")
    print ("LCM:",lcmofValues,"")
    print ("Prime Status:",isPrime,"")
    rerun = input("Would you like to rerun this program?(y/n)")
else: 
    print("Bye, Have a great day!")
