enteredText = input("enter your text here: ")

numberValue = []
stringValue = []
unknownValue = []


def typeSeperator(text):
    seperatedValues = text.split(" ")
    for value in seperatedValues:
        if not value.isdigit():
            stringValue.append(value)
        elif value.isnumeric():
            numberValue.append(value)
        else:
            unknownValue.append(value)

    #finalListOfWords = list(" ".join(stringValue))
    #finalListOfNumbers = list(" ".join(numberValue))
    print(f"words: {stringValue}")
    print(f"numbers: {numberValue}")
    if len(unknownValue) != 0 or []:
        print(f"and it also includes {unknownValue} as another value type")
    else: 
        print("and there is not any unknown type")

typeSeperator(enteredText)
