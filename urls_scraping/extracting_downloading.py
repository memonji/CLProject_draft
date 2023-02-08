import os
import requests
import re
from urllib import request
import nltk
import string
from nltk.stem import WordNetLemmatizer
#%%
title = 'Ulysses'
author = 'James Joyce'
url = 'https://www.gutenberg.org/files/4300/4300-0.txt'
path = '/Users/renato/PycharmProjects/CLProject/corpus/'


def find_text(raw):
    pass

def text_from_gutenberg(title, author, url, path = '/Users/renato/PycharmProjects/CLProject/corpus/', return_raw = False, return_tokens = False):
    # Convert inputs to lowercase
    title = title.lower()
    author = title.lower()

    # Check if the file is stored locally
    filename = '/Users/renato/PycharmProjects/CLProject/corpus/' + title
    if os.path.isfile(filename) and os.stat(filename).st_size != 0:
        print("{title} file already exists".format(title=title))
        print(filename)
        with open(filename, 'r') as f:
            raw = f.read()

    else:
        print("{title} file does not already exist. Grabbing from Project Gutenberg".format(title=title))
        response = request.urlopen(url)
        raw = response.read().decode('utf-8-sig')
        print("Saving {title} file".format(title=title))
        with open(filename, 'w') as outfile:
            outfile.write(raw)

    if return_raw:
        return raw

    # Option to return tokens
    if return_tokens:
        return nltk.word_tokenize(find_text(raw))

    else:
        return find_beginning_and_end(raw)
#%%
def find_beginning_and_end(raw):
    '''
    This function serves to find the text within the raw data provided by Project Gutenberg
    '''

    start_regex = '\*\*\*\s?START OF TH(IS|E) PROJECT GUTENBERG EBOOK.*\*\*\*'
    draft_start_position = re.search(start_regex, raw)
    begining = draft_start_position.end()

    if re.search(title.lower(), raw[draft_start_position.end():].lower()):
        title_position = re.search(title.lower(), raw[draft_start_position.end():].lower())
        begining += title_position.end()
        # If the title is present, check for the author's name as well
        if re.search(author.lower(), raw[draft_start_position.end() + title_position.end():].lower()):
            author_position = re.search(author.lower(), raw[draft_start_position.end() + title_position.end():].lower())
            begining += author_position.end()

    end_regex = 'end of th(is|e) project gutenberg ebook'
    end_position = re.search(end_regex, raw.lower())

    text = raw[begining:end_position.start()]

    return text
#%%
title = 'Moby-Dick'
author = 'Herman Melville'
url = 'https://www.gutenberg.org/cache/epub/2489/pg2489.txt'
path = '/Users/renato/PycharmProjects/CLProject/corpus/'
melville_mobydick_text = text_from_gutenberg(title, author, url)
print (melville_mobydick_text[:1000])
#%%
def preprocessing(text):
    lower_text = text.lower()
    no_punct_corpus = lower_text.translate(str.maketrans("", "", string.punctuation))
    no_number_corpus = re.sub(r'\d+', '', no_punct_corpus)
    tokenized_corpus = nltk.word_tokenize(no_number_corpus)
    lemmatizer = WordNetLemmatizer()
    lemmatized_corpus = " ".join([lemmatizer.lemmatize(word) for word in tokenized_corpus])

    return lemmatized_corpus
#%%
title = 'Moby-Dick'
author = 'Herman Melville'
url = 'https://www.gutenberg.org/cache/epub/2489/pg2489.txt'
path = '/Users/renato/PycharmProjects/CLProject/corpus/'
melville_mobydick_text = preprocessing(text_from_gutenberg(title, author, url))
print(melville_mobydick_text)

filename = f"{path}lemmatized_{title.lower().replace('-', '')}.txt"
with open(filename, "w") as f:
    f.write(melville_mobydick_text)
