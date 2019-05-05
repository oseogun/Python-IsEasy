"""
Python code to demonstrate lists
Script sorts values provided into two categories "my unique list" & "my left overs"
Written by Ose Ogun, May-2019.
"""

# List to hold unique items 
myUniqueList = []

# List to hold items that already exist in myUniqueList
myLeftovers = []
   
# Adds unique values to myUniqueList and return True. If the value already exists it should return False.
def addToUniqueList(value):
    if value in myUniqueList:
        addToMyLeftOvers(value)
        print False
    else:
        myUniqueList.append(value)    

# Pushes all the rejected inputs into a separate global array called myLeftovers. 
def addToMyLeftOvers(value):
    myLeftovers.append(value)

# Test cases 
addToUniqueList(1)
addToUniqueList(2)
addToUniqueList(3)
addToUniqueList(4)
addToUniqueList(5)
addToUniqueList(1)
addToUniqueList(2)
addToUniqueList("A")
addToUniqueList("B")
addToUniqueList("C")
addToUniqueList("D")
addToUniqueList("E")
addToUniqueList("A")
addToUniqueList("B")

print myUniqueList