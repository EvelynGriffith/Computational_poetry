#!/usr/bin/env python
import random
import string
import markovify # <-- importing markovifym random, string and textwrap3
from textwrap3 import wrap

def read_file(filename):
    book = open(f"data/{filename}","r")#<-- getting the program to read through the three files in data folder
    return book.read()

def scramble(word):
    word = "".join([ch for ch in word if ch not in string.punctuation])#<-- this should delete punctuation
    if word not in keeps:#<-- see keeps list down below to see which words will not be scrambled
        scrambled = random.sample(word,len(word))#<-- scrambling words
        return "".join(scrambled)#<-- joining scrambled words
    return word

keeps = ["the", "it", "for", "and", "to", "are"] #<-- keeping certain words from being scrambled
texts = [
    "aesop.txt",
    "fairytales.txt",
    "prideandprejudice.txt"#<-- the three books I downloaded to take words from
]

text = ""#<-- defining text for later commands

scrambled = ""#<-- defining scrambled for later commands

wrapped = ""

for book in texts:#<-- getting the program to read the specific books
    text += read_file(book) + "\n"
corpus = text.split(" ")
corpus = set(corpus)
    
for word in corpus:#<-- scrambling the words and replacing words with new scrambled words
    new_word = scramble(word)
    text = text.replace(word,new_word) #<-- attempting to join text and wrap it in poem format

with open("Jabberwocky", "w") as output:
    output.write(text)