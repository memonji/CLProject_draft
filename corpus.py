import re
import nltk
import requests
import urllib.request
from bs4 import BeautifulSoup
from nltk.corpus import gutenberg
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
nltk.corpus.gutenberg.fileids()

author = "austen"
nltk.download("gutenberg")
filtered_texts = [text for text in gutenberg.fileids() if author in text]
def preprocess_text(text):
    text = BeautifulSoup(gutenberg.raw(text), "html.parser").get_text()
    text = re.sub(r"\[.*?\]", "", text)
    text = re.sub(r"[^a-zA-Z]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text
processed_texts = [preprocess_text(text) for text in filtered_texts]
tokenized_texts = [word_tokenize(text) for text in processed_texts]