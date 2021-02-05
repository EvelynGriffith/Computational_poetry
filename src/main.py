#!/usr/bin/env python

import random
from textwrap3 import wrap
import markovify
import string
    
####################################
def scramble(word):
    word = "".join([ch for ch in word if ch not in string.punctuation])
    if word not in keeps:
        scrambled = random.sample(word,len(word))
        return "".join(scrambled)
    return word

def read_file(file):
    book = open(f"data/{file}","r")
    return book.read()


keeps = ["the"]
text = [
    "aesop.txt",
    "fairytales.txt",
    "prideandprejudice.txt"
]
texts = ""

for book in text:
    texts += read_file(book) + "\n"
lines = texts.split("\n")
words = texts.split(" ")


for line in text:
    words = line.split(" ")
    for word in words:
        new_word = scramble(word)
        line = line.replace(word,new_word)
    print(line)
    

