import json
import difflib
from difflib import get_close_matches

data=json.load(open("data.json"))


def returnValue(key):
    if key in data:
        definitions=""
        if len(data[key])>1:
            for definition in data[key]:
                definitions+=definition+"\n"

            return definitions
        else: return data[key][0]

    else:
        list_of_matches=get_close_matches(key, data.keys(), 1)
        if list_of_matches:
            print("Maybe you meant {} (y/n)".format(list_of_matches[0]))
            answer=input().lower()
            if(answer=="y"): return returnValue(list_of_matches[0])
            else : return "Invalid input"
        else: return "No word like this in database."


wanna_check=True

while wanna_check:
    word = input("Enter a word you want definition for: ").lower()
    try:
        print(returnValue(word))
        print("Wanna try again? (y/n)")
        answer = input().lower()
        if answer == "n": wanna_check = False

    except:
        print("There was some issue, wanna try again? (y/n)")
        answer=input().lower()
        if answer=="n": wanna_check=False







