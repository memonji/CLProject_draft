import numpy as np
import pandas as pd
import nltk as nltk
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.stem import WordNetLemmatizer^
import re
import string

# let's pretend our corpus is substituted with the input_str by now

original_corpus = "Elephants, the oranges, the apples. The 5 biggest countries by population in 2017 are China, India, United States, Indonesia, and Brazil"

#  with open("original_corpus", "r") as f: #THIS IS AS TO OPEN OUR FUTURE CORPUS
#  corpus = f.read()

low_corpus = original_corpus.lower()  # (A) Preprocessing: (a) lowering the texts
with open("low_corpus.txt", "w") as f:
    f.write(low_corpus)

def remove_punctuation(low_corpus):  # (A) Preprocessing: (b) removing punctuation
    return low_corpus.translate(str.maketrans("", "", string.punctuation))
no_punct_corpus = remove_punctuation(low_corpus)
with open("no_punct_corpus.txt", "w") as f:
    f.write(no_punct_corpus)

#  def remove_whitespaces(no_punct_corpus):  # (A) Preprocessing: (c) removing whitespaces THIS MIGHT BE UNESSENTIAL!
    #  no_whitespace_corpus = "".join(c for c in no_punct_corpus if not c.isspace())
    #  return no_whitespace_corpus
#  no_whitespace_corpus = remove_whitespaces(no_punct_corpus)

def remove_numbers(no_punct_corpus):  # (A) Preprocessing: (d) removing numbers
    no_number_corpus = re.sub(r'\d+', '', no_punct_corpus)
    return no_number_corpus
no_number_corpus = remove_numbers(no_punct_corpus)
with open("no_number_corpus.txt", "w") as f:
    f.write(no_number_corpus)

#we might think of directly creating a file which is representing the pre-processed texts with the first steps

def tokenize_corpus(no_number_corpus): #  (B) Tokenization
    if not isinstance(no_number_corpus, str):
        no_number_corpus = str(no_number_corpus)
    tokenized_corpus = nltk.word_tokenize(no_number_corpus)
    return tokenized_corpus
tokenized_corpus = tokenize_corpus(no_number_corpus)
with open("tokenized_corpus.txt", "w") as f:
    f.write(str(tokenized_corpus))

def lemmatize_text(tokenized_corpus): #Lemmatization: we might need to use more specific filtering (but this could be done in a second moment as we precisely define the texts to use
    lemmatizer = WordNetLemmatizer()
    lemmatized_corpus = " ".join([lemmatizer.lemmatize(word) for word in tokenized_corpus])
    return lemmatized_corpus
lemmatized_cs = lemmatize_text(tokenized_corpus)
with open("lemmatized_corpus.txt", "w") as f:
    f.write(str(lemmatized_cs))


word_frequency = nltk.FreqDist(lemmatized_cs)#creating the count of frequency- it will include stop words
#print out the 10 most frequent words using the function most_common
print(word_frequency.most_common(10))



