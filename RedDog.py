# Author: Manu N 
# Date: March 3 2022
# Purpose: PY3 - Red Dog, Card Game 
 
# Libaries & Modules:
from random import randrange
from random import randint
 

# Classes: 
class TwoCard:
    def __init__ (self, card1=1, card2=1):
        self.card1 = card1
        self.card2 = card2

class Point:
    def __init__ (self, x=1, y=1):
        self.x = x
        self.y = y

# Subprograms: 
def getCard ():
    card = randint(2,14)
    return card

def getHand ():
    playerHand = TwoCard()
    playerHand.card1 = getCard()
    playerHand.card2 = getCard()
    return playerHand

def printHand (playerHandCard1, playerHandCard2):
    userCards1 = playerHandCard1 
    userCards2 = playerHandCard2  
    if (userCards1 and userCards2) <= 2 and (userCards1 and userCards2) >= 10: # Enrichment code for normal suit numbers 
        randomSuitMechanics = randrange(1,4) # This is how we generate a random number which will determine of our card is an clover, diamon, heart, or spade
        if randomSuitMechanics == 1: 
            print("♣" + userCards1 + userCards2) 
        if randomSuitMechanics == 2: 
            print("♦" + userCards1 + userCards2)
        if randomSuitMechanics == 3: 
            print("♥" + userCards1 + userCards2)
        if randomSuitMechanics == 4: 
            print("♠" + userCards1 + userCards2)
#    if (userCards1) == 0 or userCards2 == 0: # Encrichment code for Jokers (0)
#        if userCards1 == 0: 
#            userCards1 = "Joker"
#        elif userCards2 == 0: 
#            userCards2 == "Joker"
#        print(userCards1 + userCards2 + "Why you so serious?")
    if (userCards1) == 14 or userCards2 == 14: # Enrichment code for Aces (value 14)
        if userCards1 == 14: 
            userCards1 = "Ace"
        elif userCards2 == 14: 
            userCards2 = "Ace"
        print(userCards1 + userCards2)
    if (userCards1 or userCards2) == 11: # Enrichment code: Jack (value 11) 
        if userCards1 == 11: 
            userCards1 = "Jack"
        elif userCards2 == 11:
            userCards2 = "Jack"
        print(userCards1 + userCards2)
    if (userCards1 or userCards2) == 12: # Enrichment code for Queen (value 12)
        if userCards1 == 12: 
            userCards1 = "Queen"
        elif userCards2 == 12: 
            userCards2 = "Queen"
        print(userCards1 + userCards2)
    if (userCards1 or userCards2) == 13: # Enrichment code for King (value 13)
        if userCards1 == 13:
            userCards1 = "King"
        elif userCards2 == 13:
            userCards2 = "King"
        print(userCards1 + userCards2)

def handType(userCards1, userCards2):
    if userCards1 == userCards2: 
        handTypeStatus = "Pair"
    if ((userCards1 - userCards2) or (userCards2 - userCards1)) == 1:
        handTypeStatus = "Consecutive"
    if ((userCards1 - userCards2) or (userCards2 - userCards2)) != 1: 
        handTypeStatus = "Non-consecutive"

def spread(userCards1, userCards2):
    countX = userCards1
    countY = userCards2
    if countX > countY: 
        temp = countX
        countX = countY
        countY = temp
    while countX != countY: 
        countX = countX + 1
        print (countX, sep="")

#def payout(): 
    
