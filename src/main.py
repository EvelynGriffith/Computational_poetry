#!/usr/bin/env python

import random
from textwrap3 import wrap
import markovify

    
####################################
def read_file(book_name):
    book = open(f"data/{book_name}","r")
    return book.read()

keeps = ["the", "in", "to", "a", "for"]
text = [
    "aesop.txt",
    "fairytales.txt",
    "prideandprejudice.txt"
]
texts = ""

for book in text:
    text += read_file(book) + "\n"
lines = texts.split("\n")
words = texts.split(" ")

def scramble(word):
    if word not in keeps:
        scrambled = random.sample(word, len(word))
        return " ".join(scrambled)
    return word

for line in text:
    words = line.split(" ")
    for word in words:
        new_word = scramble(word)
        line = line.replace(word, new_word)

lines = [line for line in lines if line != ""]


poem.write(wrapped[0] + "\nEvelyn Griffith\n\n")

for wrap in wrapped:
    poem.write(wrap + "\n")
    
    
with open("Jabberwocky2.0", "w") as output:
    output.write(poem)