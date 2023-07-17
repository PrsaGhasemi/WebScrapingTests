enteredText = input("enter your text here: ")

numberValue = []
stringValue = []
unknownValue = []


def typeSeperator(text):
    seperatedValues = text.split()
    for value in seperatedValues:
        if value.isalpha():
            stringValue.append(value)
        elif value.isnumeric():
            numberValue.append(value)
        else:
            unknownValue.append(value)

    print(f"words: {stringValue}")
    print(f"numbers: {numberValue}")
    if len(unknownValue) != 0:
        print(f"and it also includes {unknownValue} as another value type")


typeSeperator(enteredText)
