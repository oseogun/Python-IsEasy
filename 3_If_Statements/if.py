"""
Python code to demonstrate if statement syntax.
Script compares three values and returns 'True' if any two are the same
Written by Ose Ogun, Apr-2019.
"""

# Convert string values of numbers to ther numeric values
def convertToInt(value): 
  # If value is a string value return integer equivalent
  if type(value) == str:  
    return int(value)
  else:
    return value

# Declare comparison funtion
def comparison(value1, value2, value3):
  
  # Convert any string values to its integer equivalent 
  valueOne = convertToInt(value1)
  valueTwo = convertToInt(value2)
  valueThree = convertToInt(value3)

  # Compare values to determine if any of them are equal
  if valueOne == valueTwo:
    print(True)
  elif valueOne == valueThree:
    print(True)
  elif valueTwo == valueThree:
    print(True)
  else:
    print(False) 
  
# Test Cases  
# 1. No similar values
print('-------------')
print('Test Case One Result:')
comparison(1,2,3)
print('-------------')

# 2. Similar values
print('-------------')
print('Test Case Two Result:')
comparison(1,1,3)
print('-------------')

# 3. Similar string & numeric values
print('-------------')
print('Test Case Three Result:')
comparison(1,"2",2)
print('-------------')
