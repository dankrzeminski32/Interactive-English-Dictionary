import json
from difflib import SequenceMatcher, get_close_matches

data = json.load(open("data.json"))

def definition(word):
    word = word.lower()
    if desired_word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:

         feedback = input("Did you mean %s instead? (Y/N) " % get_close_matches(word, data.keys())[0])
         if feedback == 'Y' or feedback == 'y':
             return data[get_close_matches(word, data.keys())[0]]
         else:
             return "Sorry your original word does not exist."
    else:
        return "Sorry that word does not exist in our database."


desired_word = input("Which word would you like the definition to: ")

print(definition(desired_word))

