import re

def findDates(text):
    datePattern = r'\b\d{4}/\d{2}/\d{2}\b'
    dates = re.findall(datePattern, text)
    
    return dates

textInput = input("Enter Your text here: ") 
extractedDates = findDates(textInput)
if extractedDates:
    for date in extractedDates:
            print(f"{date} \n")
else:
    print("No dates in the form of yyyy/mm/dd found in the input.")
