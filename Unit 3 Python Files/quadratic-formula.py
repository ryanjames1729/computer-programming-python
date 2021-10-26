# CDS - Programming
# Quadratic Formula Assignment
#
# Student Name: 

# This function has input given as a string representation of the quadratic formula
# This function should return a list of 3 integers that are the numbers from the string
def stripFormula(string):
  outputList = []   # this list should hold the numbers: a, b, and c
  # string = "ax^2 + bx + c = 0"
  index = string.find("x^2")
  print(index)
  a = string[index-1]
  outputList.append(int(a))
  string = string[index+1:]
  index = string.find("x")
  print(index)
  b = string[index-1]
  string = string[index+1:]
  outputList.append(int(b))
  index = string.find("=")
  print(index)
  c = string[index-1]
  outputList.append(int(c))
  return outputList


# This function has input as 3 integers
# This function should return the determinant: b^2-4ac  
def discriminant(a, b, c):
  return 

# This function has input as 3 integers
# This function should return a string representation of the solution. It should call the function 'determinant'.
def getZeros(a, b, c):
  
    return 

expression = input("Give me a quadratic expression:>>").strip()

