import string  #Using Other Modules in a Module
import random

def generateFullName(firstName = "" , lastName = ""):
    fullName = firstName + ' ' + lastName
    return fullName

def generateGreeting(name):
    print(f"Hello {name}, How Are You? ")


def generateStrongPassword(passLen = 5):
    alphabets = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    allText = alphabets + digits + symbols
    passList = []
    for i in range(passLen):
        passList.append(allText[random.randint(0, len(allText)-1)])

    print(''.join(passList))
        