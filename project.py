import json
import difflib
from difflib import get_close_matches
data=json.load(open("data.json"))

def ReturnValue(key):
    if key in data:
        return data[key]
    else:
        list_of_matches=get_close_matches(key, data.keys(), 3)
        if list_of_matches:
            hint="Maybe you meant one of these:\n"
            for match in list_of_matches:
                hint+= match + "\n"

            return hint
        else: return "No word like this in database."


wannaCheck=True

while wannaCheck:
    word = input("Enter a word you want definition for: ").lower()
    try:
        print(ReturnValue(word))
        print("Wanna try again? (y/n)")
        answer = input().lower()
        if answer == "n": wannaCheck = False

    except:
        print("There was some issue, wanna try again? (y/n)")
        answer=input().lower()
        if answer=="n": wannaCheck=False







