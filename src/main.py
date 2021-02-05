#!/usr/bin/env python
    
####################################
import random
import string

def read_file(filename):
    book = open(f"data/{filename}","r")
    return book.read()

def scramble(word):
    word = "".join([ch for ch in word if ch not in string.punctuation])
    if word not in keeps:
        scrambled = random.sample(word,len(word))
        return "".join(scrambled)
    return word

keeps = ["the", "it", "for", "and", "to", "are"]
texts = [
    "aesop.txt",
    "fairytales.txt",
    "prideandprejudice.txt"
]

text = ""

lines = text.split("\n")

lines = [line for line in lines if line != ""] # <---"list comprehension"
    # <-- if i print(lines) it will print it in a huge chuck cause of previous command
    
for book in texts:
    text += read_file(book) + "\n"
    
for line in text:
    words = line.split(" ")
    for word in words:
        new_word = scramble(word)
        line = line.replace(word,new_word)


poem = "\n".join(random.sample(line,20))

with open("Jabberwocky2.0", "w") as output:
    output.write(poem)