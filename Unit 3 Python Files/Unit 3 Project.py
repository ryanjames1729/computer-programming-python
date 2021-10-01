import time, os

backpack = []
wait = 3
def showBackpack():
  print("Items in my Backpack:")
  for obj in backpack:
    print(obj)
  print()

def slowText(string):
  for letter in string:
    print(letter, end="", flush=True)
    time.sleep(0.06)
  print()

def studentCenter():
  os.system('clear')
  # if "pencil" in backpack and "tape" in backpack:
  if "pencil" in backpack:
    slowText("You are in the Student Center. From here you have a few options. Where would you like to go?")
  else:
    slowText("You are in the Student Center. From here you have a few options. Where would you like to go or would you like to pick up the pencil?")
  decision = input(">>").strip().lower()
  if decision.find("hallway") > -1:
    slowText("Walking down the hallway.")
    time.sleep(wait)
    hallway()
  elif decision.find("backpack") > -1:
    time.sleep(wait)
    showBackpack()
    time.sleep(wait)
    studentCenter()
  elif decision.find("pencil") > -1 and "pencil" not in backpack:
    time.sleep(wait)
    backpack.append("pencil")
    slowText("You picked up the pencil and put it in your backpack.")
    time.sleep(wait)
    studentCenter()
  else:
    slowText("Sorry that's not an option. Let's try this again.")
    studentCenter()

def hallway():
    pass

def openDoor():
    pass

# put key in mainOffice
def mainOffice():
  pass

def stairs():
  pass

def auditorium():
  pass

def library():
  pass

def startGame():
    studentCenter()

startGame()