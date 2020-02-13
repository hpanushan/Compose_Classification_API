
from fuzzywuzzy import process
import json

def getMatchedIntent(query,optionsList):
    # This method outputs the most similar phrase with user text
    # The result will contain best matching option and it's confidence score
    result = process.extractOne(query, optionsList)

    # Output
    matched_phrase = result[0]
    matched_index = optionsList.index(matched_phrase)
    score = result[1]

    # Creating a dictionary
    dict = {'matched_phrase': matched_phrase, 'matched_index': matched_index, 'score': score}

    # Convert dict to JSON data type
    out = json.dumps(dict)

    return out

#query = 'pak 1'
#options = ['package 1', 'package 2', 'package 3']

#print(getMatchedIntent(query,options))
