enteredText = input("enter your text here: ")

def typeSeperator(text):
    seperatedValues = text.split()
    for value in seperatedValues:
        if type(value) == str