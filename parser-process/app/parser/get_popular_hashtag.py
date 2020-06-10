import json
import collections
import emoji
import re

"""
with open("larepubblica.json") as f:
    data = json.loads(f.read())
    for hashtag in data['hashtag']:
        hashtag_list += hashtag # merge all lists of hashtag in one single list
"""
# Instantiate a dictionary, and for every word in the file, 
# Add to the dictionary if it doesn't exist. If it does, increase the count.
def count_occurrences(text):
    global wordcount
    wordcount = {}
    for word in text:
        word = word.lower() # all hashtag to lower case
        word = (emoji.get_emoji_regexp().sub(u'', word)) # remove emoji
        word = re.sub(r'([?!,.://\\*]+)','', word) # remove some punctuation
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    

# print most common n_print hashtag
def get_hashtag(hashtag_list):
    #print(hashtag_list)
    final_list = []
    for hashtag_nested_list in hashtag_list:
        for hashtag in hashtag_nested_list:
            final_list.append(hashtag) # merge all lists of hashtag in one single list
    
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