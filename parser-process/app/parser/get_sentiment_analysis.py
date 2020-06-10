from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import json
import collections
import emoji
import re
import operator
import nltk
from textblob import TextBlob


def start(data):
    global sentiment_analysis_list

    sentiment_analysis_list = {}
    global comment_list 
    global most_positive_comment
    global most_negative_comment

    comment_list = []
    most_positive_comment = ""
    most_negative_comment = ""


    data = json.loads(data)
    testimonial = TextBlob(data['comment_text'][0])
    most_positive_comment = data['comment_text'][0]
    most_negative_comment = data['comment_text'][0]
    maximum = testimonial.sentiment.polarity
    minimum = testimonial.sentiment.polarity

    for comment in data['comment_text']:
        comment_list.append(comment)
        testimonial = TextBlob(comment)

        if (testimonial.sentiment.polarity > maximum):
            maximum = testimonial.sentiment.polarity
            most_positive_comment = comment

        if (testimonial.sentiment.polarity < minimum):
            minimum = testimonial.sentiment.polarity
            most_negative_comment = comment

    sentiment_analysis_list["pos_com"] = most_positive_comment
    sentiment_analysis_list["neg_com"] = most_negative_comment
    return comment_list


def sanitize(comment_list):
    it_stopwords = stopwords.words('italian')
    en_stopwords = stopwords.words('english')
    tokens = []
    final_token = []
    for comment in comment_list:
        comment = comment.lower() # all comment to lower case
        #comment = (emoji.get_emoji_regexp().sub("", comment)) # remove emoji
        comment = re.sub(r'([?!,.://({@})\\*]+)',"", comment) # remove some punctuation
        comment_tokens = word_tokenize(comment)
        tokens_without_sw = [word for word in comment_tokens if not word in it_stopwords]
        tokens_without_sw = [word for word in tokens_without_sw if not word in en_stopwords]
        tokens.append(tokens_without_sw)


    for token in tokens:
        if token:
            final_token += token

    #Create bigrams
    bgs = nltk.bigrams(final_token)
    fdist = nltk.FreqDist(bgs)
    liste = fdist.items()
    max_biagram_count = 0
    biagram_index = ""
    for x in liste:
        if x[1] > max_biagram_count:
            max_biagram_count = x[1]
            biagram_index = x[0]
    
    sentiment_analysis_list["bi_idx"] = biagram_index
    sentiment_analysis_list["bi_cnt"] = max_biagram_count

    return final_token


# Instantiate a dictionary, and for every word in the file, 
# Add to the dictionary if it doesn't exist. If it does, increase the count.
def count_occurrences(text):
    global wordcount
    wordcount = {}
    for comment in text:
        for word in comment.split():
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1
    

# print most common n_print tag
def get_comment(data):
    comment_list = start(data)
    final_list = sanitize(comment_list)
    count_occurrences(final_list)
    n_print = 10
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

    sentiment_analysis_list["pop_com"] = tmp_lista
    print(sentiment_analysis_list)
    return sentiment_analysis_list


