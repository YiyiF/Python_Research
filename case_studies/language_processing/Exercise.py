# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 21:06:33 2018

@author: eleve
"""
# E1
"""
Define hamlets as a pandas dataframe with columns language and text.
Add an if statement to check if the title is equal to 'Hamlet'.
Store the results from read_book(inputfile) to text.
Consider: How many translations are there? Which languages are they translated into?
"""
book_titles = {'English': {'shakespeare': ("A+Midsummer+Night's+Dream",
   'Hamlet',
   'Macbeth',
   'Othello',
   'Richard+III',
   'Romeo+and+Juliet',
   'The+Merchant+of+Venice')},
 'French': {'chevalier': ("L'enfer+et+le+paradis+de+l'autre+monde",
   "L'i%CC%82le+de+sable",
   'La+capitaine',
   'La+fille+des+indiens+rouges',
   'La+fille+du+pirate',
   'Le+chasseur+noir',
   'Les+derniers+Iroquois')},
 'German': {'shakespeare': ('Der+Kaufmann+von+Venedig',
   'Ein+Sommernachtstraum',
   'Hamlet',
   'Macbeth',
   'Othello',
   'Richard+III',
   'Romeo+und+Julia')},
 'Portuguese': {'shakespeare': ('Hamlet',)}}

import pandas
hamlets = pd.DataFrame(columns = ("language", "text"))
book_dir = "Books"
title_num = 1
for language in book_titles:
    for author in book_titles[language]:
        for title in book_titles[language][author]:
            if title == "Hamlet":
                inputfile = data_filepath+"Books/"+language+"/"+author+"/"+title+".txt"
                text = read_book(inputfile)
                
                
                
                
# E2
"""
Find the dictionary of word frequency in text by calling count_words_fast(). Store this as counted_text.
Create a pandas dataframe named data.
Using counted_text, define two columns in data:
word, consisting of each unique word in text.
count, consisting of the number of times each word in word is included in the text.
"""
language, text = hamlets.iloc[0]

counted_text = count_words_fast(text)

data = pd.DataFrame({
    "word": list(counted_text.keys()),
    "count": list(counted_text.values())
})        
     
     
# E3
"""
Add a column to data named length, defined as the length of each word.
Add another column named frequency, which is defined as follows for each word in data:
If count > 10, frequency is frequent.
If 1 < count <= 10, frequency is infrequent.
If count == 1, frequency is unique.
"""
language, text = hamlets.iloc[0]

counted_text = count_words_fast(text)

data = pd.DataFrame({
    "word": list(counted_text.keys()),
    "count": list(counted_text.values())
})

def frequency(count):
    if count > 10:
        return "frequent"
    elif count > 1:
        return "infrequent"
    else:
        return "unique"
        
data['length'] = data["word"].apply(len)
data['frequency']=data["count"].apply(frequency)      

# or

data.loc[data["count"] > 10,  "frequency"] = "frequent"
data.loc[data["count"] <= 10, "frequency"] = "infrequent"
data.loc[data["count"] == 1,  "frequency"] = "unique"

# E4
"""
Create a pandas dataframe named sub_data including the following columns:
    -language, which is the language of the text.
    -frequency, which is a list containing the strings "frequent", "infrequent", and "unique".
    -mean_word_length, which is the mean word length of each value in frequency.
    -num_words, which is the total number of words in each frequency category.
"""

language, text = hamlets.iloc[0]

counted_text = count_words_fast(text)

data = pd.DataFrame({
    "word": list(counted_text.keys()),
    "count": list(counted_text.values())
})

data["length"] = data["word"].apply(len)

data.loc[data["count"] > 10,  "frequency"] = "frequent"
data.loc[data["count"] <= 10, "frequency"] = "infrequent"
data.loc[data["count"] == 1,  "frequency"] = "unique"

# Enter your code here.
sub_data = pd.DataFrame({
    "language": language,
    "frequency": ["frequent","infrequent","unique"],
    "mean_word_length": data.groupby(by = "frequency")["length"].mean(),
    "num_words": data.groupby(by = "frequency").size()
})

# E5
"""

"""

def summarize_text(language, text):
    counted_text = count_words_fast(text)

    data = pd.DataFrame({
        "word": list(counted_text.keys()),
        "count": list(counted_text.values())
    })
    
    data.loc[data["count"] > 10,  "frequency"] = "frequent"
    data.loc[data["count"] <= 10, "frequency"] = "infrequent"
    data.loc[data["count"] == 1,  "frequency"] = "unique"
    
    data["length"] = data["word"].apply(len)
    
    sub_data = pd.DataFrame({
        "language": language,
        "frequency": ["frequent","infrequent","unique"],
        "mean_word_length": data.groupby(by = "frequency")["length"].mean(),
        "num_words": data.groupby(by = "frequency").size()
    })
    
    return(sub_data)
    
# Enter your code here.
grouped_data = pd.DataFrame(columns = ["language", "frequency",
                                       "mean_word_length", "num_words"])
for indices in hamlets.index:
    language, text = hamlets.iloc[indices-1]
    sub_data = sub_data.append(summarize_text(language, text))
    
# E6
"""
Plot the word statistics of each translations on a single plot. 
"""

colors = {"Portuguese": "green", "English": "blue", "German": "red"}
markers = {"frequent": "o","infrequent": "s", "unique": "^"}
import matplotlib.pyplot as plt
for i in range(grouped_data.shape[0]):
    row = grouped_data.iloc[i]
    plt.plot(row.mean_word_length, row.num_words,
        marker=markers[row.frequency],
        color = colors[row.language],
        markersize = 10
    )

color_legend = []
marker_legend = []
for color in colors:
    color_legend.append(
        plt.plot([], [],
        color=colors[color],
        marker="o",
        label = color, markersize = 10, linestyle="None")
    )
for marker in markers:
    marker_legend.append(
        plt.plot([], [],
        color="k",
        marker=markers[marker],
        label = marker, markersize = 10, linestyle="None")
    )
plt.legend(numpoints=1, loc = "upper left")

plt.xlabel("Mean Word Length")
plt.ylabel("Number of Words")
# show your plot using `plt.show`!
plt.show()
