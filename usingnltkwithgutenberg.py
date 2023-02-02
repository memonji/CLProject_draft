import re
import nltk
import requests
from bs4 import BeautifulSoup
from nltk.corpus import gutenberg
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords


nltk.download('punkt')
nltk.download('stopwords')

nltk.corpus.gutenberg.fileids()  # list of files from project gutenberg

emma = nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))  # word context
emma.concordance("surprize")

for fileid in gutenberg.fileids():  # giving some measures of texts
    num_chars = len(gutenberg.raw(fileid))  # 1st measure of characters
    num_words = len(gutenberg.words(fileid))  # first column is the average words length
    num_sents = len(gutenberg.sents(fileid))  # 2nd average sentence length (num words/num sents)
    num_vocab = len(set(w.lower() for w in gutenberg.words(fileid)))
    print(round(num_chars / num_words), round(num_words / num_sents), round(num_words / num_vocab), fileid)

BlakePoems = gutenberg.sents('blake-poems.txt')
for i in range(0, len(BlakePoems)):  # selecting words to print
    if len(BlakePoems[i]) == 10:
        print(BlakePoems[i])

url = 'https://www.gutenberg.org/cache/epub/2264/pg2264.txt'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
text = soup.get_text()
words = re.findall('\w+', text)  # reading the text words by word
lowered = []  # lowercasing al the words
for word in words:
    lowered.append(word.lower())
text = nltk.FreqDist(lowered)
fdist = nltk.FreqDist(text)
fdist.plot(30)


def gutenberg_plot(url, n):  # in order to have the possibility of changing the file
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()
    words = re.findall('\w+', text)  # reading the text words by word
    lowered = []  # lowercasing al the words
    for word in words:
        lowered.append(word.lower())
    text = nltk.Text(lowered)
    fdist = nltk.FreqDist(text)
    fdist.plot(num_vocab)
gutenberg_plot('https://www.gutenberg.org/cache/epub/2264/pg2264.txt', 20)

url = "http://www.gutenberg.org/files/15784/15784-0.txt"  # scraping
response = requests.get(url)
soup_dos = BeautifulSoup(response.content, "html.parser")
dos_text = soup_dos.get_text()
ds = 'D\w+'
tokenizer = RegexpTokenizer('\w+')
tokens = tokenizer.tokenize(dos_text)
words = []
for word in tokens:
    words.append(word.lower())
stop_words = set(stopwords.words('english'))
filter_text = [word for word in words if not word in stop_words ]
var = filter_text[:10]

len(text)  #lexical richness
len(set(text))/len(text)