# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 17:44:45 2018

@author: eleve
"""

text = "This is my test text. We're keeping this text short to keep things manageable."

def count_words(text):
    """
    Count the number of times each word occurs in text (str). Return dictionary
    where keys are unique words and values are word counts. Skip punctuations.
    """
    # lowercase
    text = text.lower()
    #Skip punctuations for loop
    skips = [".", ",", ";", ":", "'",'"']
    for ch in skips:
        #Skip the punctuations
        text = text.replace(ch, "")
    #dict word_counts
    word_counts = {}
    #count the times for loop
    for word in text.split(" "):
        #known word
        if word in word_counts:
            word_counts[word] += 1
        #unknown word
        else:
            word_counts[word] = 1
    return word_counts
        
    
from collections import Counter

def count_words_fast(text):
    """
    Count the number of times each word occurs in text (str). Return dictionary
    where keys are unique words and values are word counts. Skip punctuations.
    """
    # lowercase
    text = text.lower()
    #Skip punctuations for loop
    skips = [".", ",", ";", ":", "'",'"']
    for ch in skips:
        #Skip the punctuations
        text = text.replace(ch, "")
    #dict word_counts
    word_counts = Counter(text.split(" "))
    return word_counts
    

count_words(text) == count_words_fast(text)

count_words(text) is count_words_fast(text)





def read_book(title_path):
    """
    Read a book and return it as a string.
    """
    with open(title_path, "r", encoding="utf8") as current_file:
        text = current_file.read()
        text = text.replace("\n", "").replace("\r", "")
    return text

#call
text = read_book("E:\python_case_studies\language_processing\Books\English\shakespeare\Romeo and Juliet.txt")
len(text)
ind = text.find("What's in a name?")


def word_stats(word_counts):
    """Return number of nuique word and frequencies."""
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)


text = read_book("E:\python_case_studies\language_processing\Books\English\shakespeare\Romeo and Juliet.txt")
word_counts = count_words(text)
(num_unique, counts) = word_status(word_counts)
print(num_unique, sum(counts))

text = read_book("E:\python_case_studies\language_processing\Books\German\shakespeare\Romeo und Julia.txt")
word_counts = count_words(text)
(num_unique, counts) = word_status(word_counts)
print(num_unique, sum(counts))



import os
book_dir = "E:\python_case_studies\language_processing\Books"
#os.listdir(book_dir)
import pandas as pd
stats = pd.DataFrame(columns = ("language", "author", "title", "length", "unique"))
title_num = 1

for language in os.listdir(book_dir):
    for author in os.listdir(book_dir + "/" + language):
        for title in os.listdir(book_dir + "/" + language + "/" + author):
            inputfile = book_dir + "/" + language + "/" + author + "/" + title
            print(inputfile)
            text = read_book(inputfile)
            (num_unique, counts) = word_stats(count_words(text))
            stats.loc[title_num] = language, author.capitalize(), title.replace(".txt", ""), sum(counts), num_unique
            title_num += 1

stats.head()
stats.tail()

#   3.2.6

import matplotlib.pyplot as plt
plt.plot(stats.length, stats.unique, "bo")
plt.loglog(stats.length, stats.unique, "bo")
stats[stats.language == "English"]
stats[stats.language == "French"]

plt.figure(figsize = (10, 10))
subset = stats[stats.language == "English"]
plt.loglog(subset.length, subset.unique, "o", label = "English", color = "crimson")
subset = stats[stats.language == "French"]
plt.loglog(subset.length, subset.unique, "o", label = "French", color = "forestgreen")
subset = stats[stats.language == "German"]
plt.loglog(subset.length, subset.unique, "o", label = "German", color = "orange")
subset = stats[stats.language == "Portuguese"]
plt.loglog(subset.length, subset.unique, "o", label = "Portuguese", color = "blueviolet")

plt.legend()
plt.xlabel("Book length")
plt.ylabel("Number of unique words")
plt.savefig("lang_plot.pdf")

#Exercise Case Studies 2

hamlets = pd.DataFrame(columns = ("language", "text"))
book_dir = "E:\python_case_studies\language_processing\Books"
title_num = 1
for language in book_titles:
    for author in book_titles[language]:
        for title in book_titles[language][author]:
            if title == "Hamlet":
                inputfile = data_filepath+"Books/"+language+"/"+author+"/"+title+".txt"
                text = read_book(inputfile)
                hamlets.loc[title_num] = language, text
                title_num += 1


























#   3.2.5
import pandas as pd
table = pd.DataFrame(columns = ("name", "age"))
table.loc[1] = "James", 22
table.loc[2] = "Jess", 32
table.columns


































