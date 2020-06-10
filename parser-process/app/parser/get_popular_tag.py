import json
import collections
import re


"""
tag_list = []
with open("larepubblica.json") as f:
    data = json.loads(f.read())
    for tag in data['tag']:
        tag_list += tag # merge all lists of hashtag in one single list

"""

# Instantiate a dictionary, and for every word in the file, 
# Add to the dictionary if it doesn't exist. If it does, increase the count.
def count_occurrences(text):
    global wordcount
    wordcount = {}
    for word in text:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    

# print most common n_print tag
def get_tag(tag_list):
    final_list = []
    for tag_nested_list in tag_list:
        for tag in tag_nested_list:
            final_list.append(tag) # merge all lists of tag in one single list
    
    count_occurrences(final_list)
    n_print = 5
    tmp_lista = []
    word_list = []
    count_list = []
    word_counter = collections.Counter(wordcount)
    for word, count in word_counter.most_common(n_print):
        #print(word + " : " + str(count))
        word_list.append(word)
        count_list.append(count)

    tmp_lista.append(word_list)
    tmp_lista.append(count_list)
    return tmp_lista
