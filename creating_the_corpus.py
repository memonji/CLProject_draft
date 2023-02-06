# import nltk
# import random
# import pickle
# nltk.download('sklearn')
# nltk.download('sklearnClassifier')
# from nltk.classify.scikitlearn import sklearnClassifier

# # # # # documents = []
# # # # # for category in movie_reviews.categories():
# # # # #     for fileid in movie_reviews.fileids(category):
# # # # #         documents.append(list(movie_reviews.words(fileid)), category)
# # # # random.shuffle(documents)
# # # # print(documents[1])
# # # # all_words = []
# # # # for w in movie_reviews.words():
# # # #     all_words.append(w.lower())
# # # # all_words = nltk.FreqDist(all_words)
# # # # print(all_words("stupid"))

# for w in movie_reviews.words():
#     all_words.append(w.lower())
# all_wprds = nltk.FreqDist(all_words)
# word_features = list(all_words.keys()) [:3000]
# def find_features(document):
#     words = set(document)
#     features = {}
#     for w in word_features:
#         features[w] = (w in words)

# url = 'http://www.gutenberg.org/cache/epub/2264/pg2264.txt'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
# text = soup.get_text()
# words = re.findall('\w+', text)
# lowered =[]
# for word in words:
#     lowered.append(word.lower())
# text = nltk.Text(lowered)
# fdist = nltk.FreqDist(text)
# fdist.plot(30)

# def gutenberg_plot(url,n): # from url getting informations from the page
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser') # response into soup object
#     text = soup.get_text()
#     words = re.findall('\w+', text) # extracting the words
#     lowered = []
#     for word in words:
#         lowered.append(word.lower())
#     text = nltk.Text(lowered) # turn the words in nltk objects
#     fdlist = nltk.FreqDist(text) # create a frequency distribution
#     fdlist.plot(n)

import requests

# Open the text file in write mode
with open("urls.txt", "w") as melville_file:
    # List of URLs
    urls = ["https://www.gutenberg.org/cache/epub/2489/pg2489.txt", 
    "https://www.gutenberg.org/cache/epub/2694/pg2694.txt", 
    "https://www.gutenberg.org/cache/epub/4045/pg4045.txt", 
    "https://www.gutenberg.org/cache/epub/10712/pg10712.txt", 
    'https://www.gutenberg.org/cache/epub/11231/pg11231.txt', 
    'https://www.gutenberg.org/cache/epub/12384/pg12384.txt', 
    'https://www.gutenberg.org/cache/epub/12384/pg12384.txt', 
    'https://www.gutenberg.org/cache/epub/34970/pg34970.txt',
    'https://www.gutenberg.org/cache/epub/21816/pg21816.txt',
    'https://www.gutenberg.org/cache/epub/15859/pg15859.txt',
    'https://www.gutenberg.org/cache/epub/15422/pg15422.txt',
    'https://www.gutenberg.org/cache/epub/13721/pg13721.txt',
    'https://www.gutenberg.org/cache/epub/13720/pg13720.txt']
    # Iterate through the list of URLs
    for url in urls:
        # Make a request to the URL
        response = requests.get(url)
        # Check if the request was successful
        if response.status_code == 200:
            # Write the response text to the text file, followed by a new line
            melville_file.write(response.text + "\n")
# # Open the text file in read mode
# with open("urls.txt", "r") as melville_file:
#     # Read the contents of the file into a string
#     contents = melville_file.read()
#     # Print the contents of the file
#     print(contents)

with open("urls.txt", "w") as thoreau_file:
    # List of URLs
    urls = [    "https://www.gutenberg.org/cache/epub/4066/pg4066.txt",    "https://www.gutenberg.org/cache/epub/4232/pg4232.txt",    "https://www.gutenberg.org/cache/epub/9846/pg9846.txt",    "https://www.gutenberg.org/cache/epub/34392/pg34392.txt",    "https://www.gutenberg.org/cache/epub/34990/pg34990.txt",    "https://www.gutenberg.org/cache/epub/42500/pg42500.txt",    "https://www.gutenberg.org/cache/epub/60951/pg60951.txt",    "https://www.gutenberg.org/cache/epub/2567/pg2567.txt",    "https://www.gutenberg.org/cache/epub/63459/pg63459.txt"]
    # Iterate through the list of URLs
    for url in urls:
        # Make a request to the URL
        response = requests.get(url)
        # Check if the request was successful
        if response.status_code == 200:
            # Write the response text to the text file, followed by a new line
            thoreau_file.write(response.text + "\n")
# # Open the text file in read mode
# with open("urls.txt", "r") as thoreau_file:
#     # Read the contents of the file into a string
#     contents = thoreau_file.read()
#     # Print the contents of the file
#     print(contents)

#optimizing
import requests

def write_urls_to_file(urls, file_name):
    # Open the text file in write mode
    with open(file_name, "w") as file:
        # Iterate through the list of URLs
        for url in urls:
            # Make a request to the URL
            response = requests.get(url)
            # Check if the request was successful
            if response.status_code == 200:
                # Write the response text to the text file, followed by a new line
                file.write(response.text + "\n")

# List of URLs for Melville
melville_urls = [
    "https://www.gutenberg.org/cache/epub/2489/pg2489.txt", 
    "https://www.gutenberg.org/cache/epub/2694/pg2694.txt", 
    "https://www.gutenberg.org/cache/epub/4045/pg4045.txt", 
    "https://www.gutenberg.org/cache/epub/10712/pg10712.txt", 
    'https://www.gutenberg.org/cache/epub/11231/pg11231.txt', 
    'https://www.gutenberg.org/cache/epub/12384/pg12384.txt', 
    'https://www.gutenberg.org/cache/epub/12384/pg12384.txt', 
    'https://www.gutenberg.org/cache/epub/34970/pg34970.txt',
    'https://www.gutenberg.org/cache/epub/21816/pg21816.txt',
    'https://www.gutenberg.org/cache/epub/15859/pg15859.txt',
    'https://www.gutenberg.org/cache/epub/15422/pg15422.txt',
    'https://www.gutenberg.org/cache/epub/13721/pg13721.txt',
    'https://www.gutenberg.org/cache/epub/13720/pg13720.txt'
]

# List of URLs for Thoreau
thoreau_urls = [   
    "https://www.gutenberg.org/cache/epub/4066/pg4066.txt",   
    "https://www.gutenberg.org/cache/epub/4232/pg4232.txt",   
    "https://www.gutenberg.org/cache/epub/9846/pg9846.txt",   
    "https://www.gutenberg.org/cache/epub/34392/pg34392.txt",   
    "https://www.gutenberg.org/cache/epub/34990/pg34990.txt",   
    "https://www.gutenberg.org/cache/epub/42500/pg42500.txt",   
    "https://www.gutenberg.org/cache/epub/60951/pg60951.txt",   
    "https://www.gutenberg.org/cache/epub/2567/pg2567.txt",   
    "https://www.gutenberg.org/cache/epub/63459/pg.txt" 
]

poe_urls = ["https://www.gutenberg.org/cache/epub/2148/pg2148.txt",
            'https://www.gutenberg.org/cache/epub/2147/pg2147.txt',
            'https://www.gutenberg.org/cache/epub/17192/pg17192.txt',
            'https://www.gutenberg.org/cache/epub/2151/pg2151.txt',
            'https://www.gutenberg.org/files/2149/2149-0.txt',
            'https://www.gutenberg.org/files/2150/2150-0.txt',
            'https://www.gutenberg.org/files/32037/32037-0.txt',
            'https://www.gutenberg.org/cache/epub/2151/pg2151.txt']

hawthorne_urls = ['https://www.gutenberg.org/cache/epub/976/pg976.txt',
                'https://www.gutenberg.org/files/1916/1916-0.txt',
                'https://www.gutenberg.org/cache/epub/2081/pg2081.txt',
                'https://www.gutenberg.org/files/2181/2181-0.txt',
                'https://www.gutenberg.org/files/2182/2182-0.txt',
                'https://www.gutenberg.org/cache/epub/7085/pg7085.txt',
                'https://www.gutenberg.org/cache/epub/7119/pg7119.txt',
                'https://www.gutenberg.org/files/7183/7183-0.txt',
                'https://www.gutenberg.org/cache/epub/7372/pg7372.txt',
                'https://www.gutenberg.org/cache/epub/7878/pg7878.txt',
                'https://www.gutenberg.org/cache/epub/7881/pg7881.txt',
                'https://www.gutenberg.org/cache/epub/8088/pg8088.txt',
                'https://www.gutenberg.org/cache/epub/8089/pg8089.txt',
                'https://www.gutenberg.org/cache/epub/8090/pg8090.txt',
                'https://www.gutenberg.org/files/8091/8091-0.txt',
                'https://www.gutenberg.org/cache/epub/8429/pg8429.txt',
                'https://www.gutenberg.org/cache/epub/9201/pg9201.txt',
                'https://www.gutenberg.org/cache/epub/9202/pg9202.txt',
                'https://www.gutenberg.org/cache/epub/9203/pg9203.txt',
                'https://www.gutenberg.org/files/9204/9204-0.txt',
                'https://www.gutenberg.org/cache/epub/9205/pg9205.txt',
                'https://www.gutenberg.org/cache/epub/9206/pg9206.txt',
                'https://www.gutenberg.org/cache/epub/9207/pg9207.txt',
                'https://www.gutenberg.org/cache/epub/9208/pg9208.txt',
                'https://www.gutenberg.org/cache/epub/9209/pg9209.txt',
                'https://www.gutenberg.org/cache/epub/9210/pg9210.txt',
                'https://www.gutenberg.org/files/9211/9211-0.txt',
                'https://www.gutenberg.org/cache/epub/9212/pg9212.txt',
                'https://www.gutenberg.org/files/9213/9213-0.txt',
                'https://www.gutenberg.org/files/9214/9214-0.txt',
                'https://www.gutenberg.org/files/9215/9215-0.txt',
                'https://www.gutenberg.org/cache/epub/9216/pg9216.txt',
                'https://www.gutenberg.org/files/9217/9217-0.txt',
                'https://www.gutenberg.org/cache/epub/9218/pg9218.txt',
                'https://www.gutenberg.org/cache/epub/9219/pg9219.txt',
                'https://www.gutenberg.org/files/9220/9220-0.txt',
                'https://www.gutenberg.org/cache/epub/512/pg512.txt',
                'https://www.gutenberg.org/cache/epub/9222/pg9222.txt',
                'https://www.gutenberg.org/cache/epub/9236/pg9236.txt',
                'https://www.gutenberg.org/cache/epub/9237/pg9237.txt',
                'https://www.gutenberg.org/cache/epub/9238/pg9238.txt',
                'https://www.gutenberg.org/cache/epub/9239/pg9239.txt',
                'https://www.gutenberg.org/cache/epub/9240/pg9240.txt',
                'https://www.gutenberg.org/cache/epub/9241/pg9241.txt',
                'https://www.gutenberg.org/cache/epub/9242/pg9242.txt',
                'https://www.gutenberg.org/cache/epub/9243/pg9243.txt',
                'https://www.gutenberg.org/cache/epub/9244/pg9244.txt',
                'https://www.gutenberg.org/cache/epub/9246/pg9246.txt',
                'https://www.gutenberg.org/files/9247/9247-0.txt',
                'https://www.gutenberg.org/files/9248/9248-0.txt',
                'https://www.gutenberg.org/cache/epub/9249/pg9249.txt',
                'https://www.gutenberg.org/cache/epub/9250/pg9250.txt',
                'https://www.gutenberg.org/files/9251/9251-0.txt',
                'https://www.gutenberg.org/cache/epub/9252/pg9252.txt',
                'https://www.gutenberg.org/cache/epub/9253/pg9253.txt',
                'https://www.gutenberg.org/files/9255/9255-0.txt',
                'https://www.gutenberg.org/files/9256/9256-0.txt',
                'https://www.gutenberg.org/files/9257/9257-0.txt',
                'https://www.gutenberg.org/files/9258/9258-0.txt',
                'https://www.gutenberg.org/files/15697/15697-0.txt',
                'https://www.gutenberg.org/files/64944/64944-0.txt',
                'https://www.gutenberg.org/files/77/77-0.txt',
                'https://www.gutenberg.org/cache/epub/41368/pg41368.txt',
                'https://www.gutenberg.org/cache/epub/33/pg33.txt',
                'https://www.gutenberg.org/cache/epub/30376/pg30376.txt',
                'https://www.gutenberg.org/cache/epub/41309/pg41309.txt',
                ]
# Hawthorne Nataniel_list: Tanglewood Tales, The Great Stone Face, and Other Tales of the White Mountains,  The Blithedale Romance, The Marble Faun; Or, The Romance of Monte Beni - Volume 1, The Marble Faun; Or, The Romance of Monte Beni - Volume 2, Fanshawe, The Dolliver Romance, Doctor Grimshawe's Secret — a Romance, Septimius Felton, or, the Elixir of Life, Passages from the English Notebooks, Complete; Passages from the French and Italian Notebooks, Complete; Passages from the American Notebooks, Volume 1; Passages from the American Notebooks, Volume 2.; Our Old Home: A Series of English Sketches; Sketches and Studies; The Ancestral Footstep (fragment) Outlines of an English Romance; various pieces from Twice Told Tales; A Rill from the Town Pump; A Select Party; various pieces from The Snow Image and Other Twice-Told Tales; A Bell's Biography; various pieces from The Doliver Romance and Other Pieces: Tales and Sketches; A Book of Autographs; various pieces from A Wonder-book for girls and boys; "Browne's Folly" (From: "The Doliver Romance and Other Pieces: Tales and Sketches"); True Stories of History and Biography; In colonial days; The House of the Seven Gables; Mosses from an old manse; Love Letters of Nathaniel Hawthorne, Volume 2 (of 2); The Scarlet Letter; The snow-image: a childish miracle;  Love Letters of Nathaniel Hawthorne, Volume 1 (of 2);                   

dickinson_urls = ['https://www.gutenberg.org/cache/epub/12242/pg12242.txt']

import os
import requests

# Create the "coding" directory if it doesn't exist
coding_dir = "coding"
if not os.path.exists(coding_dir):
    os.makedirs(coding_dir)

# Open the text file in write mode
file_path = os.path.join(coding_dir, "melville_file.txt")
with open(file_path, "w") as melville_file:
    # List of URLs
    urls = [
        "https://www.gutenberg.org/cache/epub/2489/pg2489.txt", 
        "https://www.gutenberg.org/cache/epub/2694/pg2694.txt", 
        "https://www.gutenberg.org/cache/epub/4045/pg4045.txt", 
        # ...
    ]
    # Iterate through the list of URLs
    for url in urls:
        # Make a request to the URL
        response = requests.get(url)
        # Check if the request was successful
        if response.status_code == 200:
            # Write the response text to the text file, followed by a new line
            melville_file.write(response.text + "\n")

# Open another text file in write mode
file_path = os.path.join(coding_dir, "thoreau_file.txt")
with open(file_path, "w") as thoreau_file:
    # List of URLs
    urls = [
        "https://www.gutenberg.org/cache/epub/4066/pg4066.txt", 
        "https://www.gutenberg.org/cache/epub/4232/pg4232.txt", 
        # ...
    ]
    # Iterate through the list of URLs
    for url in urls:
        # Make a request to the URL
        response = requests.get(url)
        # Check if the request was successful
        if response.status_code == 200:
            # Write the response text to the text file, followed by a new line
            thoreau_file.write(response.text + "\n")

import requests
import os

# Create "coding" folder if it doesn't exist
if not os.path.exists("coding"):
    os.makedirs("coding")

def write_to_file(file_name, urls):
    with open(f"coding/{file_name}.txt", "w") as file:
        for url in urls:
            response = requests.get(url)
            if response.status_code == 200:
                file.write(response.text + "\n")

# Write the URLs to "melville.txt" in the "coding" folder
melville_urls = ["https://www.gutenberg.org/cache/epub/2489/pg2489.txt",
                 "https://www.gutenberg.org/cache/epub/2694/pg2694.txt",
                 "https://www.gutenberg.org/cache/epub/4045/pg4045.txt",
                 "https://www.gutenberg.org/cache/epub/10712/pg10712.txt",
                 'https://www.gutenberg.org/cache/epub/11231/pg11231.txt',
                 'https://www.gutenberg.org/cache/epub/12384/pg12384.txt',
                 'https://www.gutenberg.org/cache/epub/12384/pg12384.txt',
                 'https://www.gutenberg.org/cache/epub/34970/pg34970.txt',
                 'https://www.gutenberg.org/cache/epub/21816/pg21816.txt',
                 'https://www.gutenberg.org/cache/epub/15859/pg15859.txt',
                 'https://www.gutenberg.org/cache/epub/15422/pg15422.txt',
                 'https://www.gutenberg.org/cache/epub/13721/pg13721.txt',
                 'https://www.gutenberg.org/cache/epub/13720/pg13720.txt']
write_to_file("melville", melville_urls)

# Write the URLs to "thoreau.txt" in the "coding" folder
thoreau_urls = ["https://www. etc

# a list of documents
docs = ['prefix-document1-suffix', 'prefix-document2-suffix', 'prefix-document3-suffix']

# the prefix and suffix to remove
prefix = 'prefix-'
suffix = '-suffix'

# looping through the list of documents
for i in range(len(docs)):
    # removing the prefix and suffix from each document
    docs[i] = docs[i][len(prefix):-len(suffix)]

# the updated list of documents
print(docs)

# a list of documents
docs = ['document1 before target1 after target2 before target1 after', 
        'document2 before target1 after target2 before target1 after', 
        'document3 before target1 after target2 before target1 after']

# the sentences to use as markers
start_sentence = "before target1"
end_sentence = "after target2"

# looping through the list of documents
for i in range(len(docs)):
    # splitting the document into parts based on the start and end sentences
    parts = docs[i].split(start_sentence)
    parts = parts[1].split(end_sentence)
    # updating the document with the part between the start and end sentences
    docs[i] = start_sentence + parts[0] + end_sentence

# the updated list of documents
print(docs)
