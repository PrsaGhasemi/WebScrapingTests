from fuzzywuzzy import fuzz

string1 = input("enter the first text: ")
string2 = input("enter the second text: ")
def compareMachine(firstText , secondText):
    compare = fuzz.ratio(firstText, secondText)
    print(f"your string are {compare}% similar")


compareMachine(string1,string2)