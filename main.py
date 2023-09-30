# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import spacy

#name of the english language model
nlp = spacy.load("en_core_web_sm")

def tokenize(text):
    doc = nlp(text)
    return [token.text for token in doc]

with open('trial.txt', 'r') as file:
    text = file.read()


tokens = tokenize(text)
print(tokens)

print("Success")