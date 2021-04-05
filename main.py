import json


data = json.load(open("data.json"))

def definition(word):
    return data[word]


desired_word = input("Which word would you like the definition to: ")

desired_word = desired_word.lower()

if desired_word in data:
    print(definition(desired_word))
else:
    print("Sorry that word does not exist in our database.")
