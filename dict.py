import json
import difflib

from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    '''
    returns the meanings of the word passed as input
    '''
    matches = get_close_matches(word,data.keys(),cutoff=0.8)
    if word in data:
        return data[word]
    elif(matches):
        yn = input(f"Did you mean : {matches[0]}? Enter y for Yes and n for NO : ")
        if yn == "y":
            return data[matches[0]]
        elif yn =="n":
            return "Alright."
        else:
            return "Invalid option."
    else:
        return "The word doesnt exist , please double check it."

word = input('Enter word : ').lower()

output = translate(word)
if type(output) == list:
    for item in output:
        print("-->"+item)
else:
    print(output)
