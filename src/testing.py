from textwrap3 import wrap
import random


def read_file(filename):
    file = open("data/Jabberwocky","r")
    return file.read()
    
files = [
    "data/Jabberwocky"
]
text = ""

for file in files:
    text += read_file(file) + "\n"

lines = text.split("\n")

lines = [line for line in lines if line != ""] # <---"list comprehension"
    # <-- if i print(lines) it will print it in a huge chuck cause of previous command

poem = "\n".join(random.sample(lines,100))

with open("output/Jabberwocky2.0", "w") as output:
    output.write(poem)