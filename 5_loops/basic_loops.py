"""
Application demonstrates basic loops in Python.
Program prints the numbers from 1 to 100.
- For multiples of three it prints "Fizz" instead. 
- For the multiples of five it prints "Buzz" instead.
- For numbers which are multiples of both three and five it prints "FizzBuzz" instead.
- For prime numbers (divisible only by itself and one) it print "Prime" instead. 
Written by Ose Ogun, May-2019.
"""

# Determine if a number is a prime number
def primeNumbers(num):
    # Test 1 - If number is less than one return false
    if(num <= 1):
        return False
    
    # Test 2 - if any lower number divides our value with no remainders retuen false 
    for i in range(2,num):
        if(num % i == 0):
            return False
          
    #If value passes all our tests return true
    return True

# Replace value in our list of numbers with appropriate string label
def replaceNumbers(value):

    if (primeNumbers(value)):
       print "Prime"

    elif ( (value % 3 == 0) and (value % 5 == 0) ):
       print "FizzBuzz"
    
    elif (value % 5 == 0):
       print "Buzz"
    
    elif (value % 3 == 0):
       print "Fizz"
    
    else: 
        print value

# Loop until a pre-specified number checks are performed 
def loop(loopLimit):     
    i = 1

    while (i <= loopLimit):
        replaceNumbers(i)
        i += 1

# Test cases 
loop(100)
