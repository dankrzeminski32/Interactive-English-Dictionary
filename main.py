import json
from difflib import SequenceMatcher, get_close_matches

data = json.load(open("data.json"))
i = 1
run_again = 'Y'
# Function to determine the definition of word by entering json file and searching for the value that matches the entered key. 
def definition(word):
    word = word.lower()
    if desired_word in data:
        return data[word]
    elif word.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[word.title()]
    elif word.upper() in data: #in case user enters words like USA or NATO
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
         feedback = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
         if feedback == 'Y' or feedback == 'y':
             return data[get_close_matches(word, data.keys())[0]]
         elif feedback == 'N' or feedback == 'n':
             return "Sorry your original word does not exist."
         else:
             return "We didn't understand your entry."
    else:
        return "Sorry that word does not exist in our database."





print("-----WELCOME TO DK ENGLISH DICTIONARY-----\n")
while run_again == 'Y' or run_again == 'y':
    desired_word = input("Which word would you like the definition to: ")
    output = (definition(desired_word))
    if isinstance(output, list):
        for item in output:
            print(i, ")",  item,)
            i = i + 1
    else:
        print(output)
    i = 1
    run_again = input("\nWould you like to search for another word? Enter Y if yes, or N if no: ")

print("Thanks for using DK ENGLISH DICTIONARY!")
   