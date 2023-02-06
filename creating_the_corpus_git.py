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

#Melville list: Moby Dick / I and my chimney / Omoo: Adventures in the South Seas / White-Jacket / Bartleby, The Scrivener
# Battle-Pieces and Aspects of the War / Pierre; or The Ambiguities / The Confidence-Man / The Piazza Tales / Israel Potter
# Mardi: and A Voyage Thither

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
                'https://www.gutenberg.org/cache/epub/41309/pg41309.txt'
                ]
# Hawthorne Nataniel_list: Tanglewood Tales, The Great Stone Face, and Other Tales of the White Mountains,  The Blithedale Romance, The Marble Faun; Or, The Romance of Monte Beni - Volume 1, The Marble Faun; Or, The Romance of Monte Beni - Volume 2, Fanshawe, The Dolliver Romance, Doctor Grimshawe's Secret — a Romance, Septimius Felton, or, the Elixir of Life, Passages from the English Notebooks, Complete; Passages from the French and Italian Notebooks, Complete; Passages from the American Notebooks, Volume 1; Passages from the American Notebooks, Volume 2.; Our Old Home: A Series of English Sketches; Sketches and Studies; The Ancestral Footstep (fragment) Outlines of an English Romance; various pieces from Twice Told Tales; A Rill from the Town Pump; A Select Party; various pieces from The Snow Image and Other Twice-Told Tales; A Bell's Biography; various pieces from The Doliver Romance and Other Pieces: Tales and Sketches; A Book of Autographs; various pieces from A Wonder-book for girls and boys; "Browne's Folly" (From: "The Doliver Romance and Other Pieces: Tales and Sketches"); True Stories of History and Biography; In colonial days; The House of the Seven Gables; Mosses from an old manse; Love Letters of Nathaniel Hawthorne, Volume 2 (of 2); The Scarlet Letter; The snow-image: a childish miracle;  Love Letters of Nathaniel Hawthorne, Volume 1 (of 2);                   
# The Wives of the Dead

dickinson_urls = ['https://www.gutenberg.org/cache/epub/12242/pg12242.txt']
# Dickinson_list = Poems: Three Series, Complete

emerson_urls = ['https://www.gutenberg.org/cache/epub/12843/pg12843.txt', 
                'https://www.gutenberg.org/cache/epub/16643/pg16643.txt',
                'https://www.gutenberg.org/cache/epub/69258/pg69258.txt'
                'https://www.gutenberg.org/cache/epub/6312/pg6312.txt',
                'https://www.gutenberg.org/cache/epub/2945/pg2945.txt']
# Emerson, Ralph Waldo_list : Poems Household Edition; Society and solitude: Twelve chapters; Representative Men: Seven Lectures; Essays by Ralph Waldo Emerson; Essays — Second Series

james_urls = ['https://www.gutenberg.org/cache/epub/69629/pg69629.txt',
            'https://www.gutenberg.org/cache/epub/209/pg209.txt',
            'https://www.gutenberg.org/cache/epub/432/pg432.txt',
            'https://www.gutenberg.org/cache/epub/1093/pg1093.txt',
            'https://www.gutenberg.org/cache/epub/1190/pg1190.txt',
            'https://www.gutenberg.org/cache/epub/1195/pg1195.txt',
            'https://www.gutenberg.org/cache/epub/2366/pg2366.txt',
            'https://www.gutenberg.org/cache/epub/2425/pg2425.txt',
            'https://www.gutenberg.org/cache/epub/2426/pg2426.txt',
            'https://www.gutenberg.org/cache/epub/2460/pg2460.txt',
            'https://www.gutenberg.org/cache/epub/2534/pg2534.txt',
            'https://www.gutenberg.org/cache/epub/4264/pg4264.txt',
            'https://www.gutenberg.org/cache/epub/7118/pg7118.txt',
            'https://www.gutenberg.org/cache/epub/8080/pg8080.txt',
            'https://www.gutenberg.org/cache/epub/8081/pg8081.txt',
            'https://www.gutenberg.org/cache/epub/19718/pg19718.txt',
            'https://www.gutenberg.org/cache/epub/19717/pg19717.txt',
            'https://www.gutenberg.org/cache/epub/20085/pg20085.txt',
            'https://www.gutenberg.org/cache/epub/25500/pg25500.txt',
            'https://www.gutenberg.org/cache/epub/26115/pg26115.txt',
            'https://www.gutenberg.org/cache/epub/28004/pg28004.txt',
            'https://www.gutenberg.org/cache/epub/29452/pg29452.txt',
            'https://www.gutenberg.org/cache/epub/30059/pg30059.txt',
            'https://www.gutenberg.org/cache/epub/32649/pg32649.txt',
            'https://www.gutenberg.org/cache/epub/32939/pg32939.txt',
            'https://www.gutenberg.org/cache/epub/33325/pg33325.txt',
            'https://www.gutenberg.org/cache/epub/37424/pg37424.txt',
            'https://www.gutenberg.org/cache/epub/37425/pg37425.txt',
            'https://www.gutenberg.org/cache/epub/38424/pg38424.txt',
            'https://www.gutenberg.org/cache/epub/55078/pg55078.txt',
            'https://www.gutenberg.org/cache/epub/68340/pg68340.txt',
            'https://www.gutenberg.org/cache/epub/68717/pg68717.txt',
            'https://www.gutenberg.org/cache/epub/68961/pg68961.txt',
            'https://www.gutenberg.org/cache/epub/69628/pg69628.txt',
            'https://www.gutenberg.org/cache/epub/179/pg179.txt',
            ]
# Henry James_list: The Princess Casamassima (Volume 2 of 2) by Henry James; The Turn of the Screw; The Ambassadors; The beast in the jungle; 
# ; The jolly corner; Glasses; The Beldonald Holbein; A bundle of letters; The diary of a man of fifty; The madonna of the future;
# ; Eugene Pickering; The golden bowl; What Maise knew; A passionate pilgrim; Louisa Pallant; The bostonians vlII; The bostonians v.1
# ; The tragic muse; A London life and others; A small boy and others; A little tour in France; The wings of the Dove v.I and II; 
# ; The middle years; The sacred fount; The spoils of poynton; Views and reviews; Within the rim and other essays; Notes of a son and a brother;
# ; The birthplace; A landspace painter; The American scene; Portraits of places; The princess Casamassima; The Europeans;

howell_urls = ['https://www.gutenberg.org/cache/epub/7359/pg7359.txt',
                'https://www.gutenberg.org/cache/epub/4646/pg4646.txt',
                'https://www.gutenberg.org/cache/epub/4600/pg4600.txt',
                'https://www.gutenberg.org/cache/epub/3406/pg3406.txt',
                'https://www.gutenberg.org/cache/epub/3405/pg3405.txt',
                'https://www.gutenberg.org/cache/epub/3388/pg3388.txt',
                'https://www.gutenberg.org/cache/epub/3376/pg3376.txt',
                'https://www.gutenberg.org/cache/epub/3375/pg3375.txt',
                'https://www.gutenberg.org/cache/epub/3365/pg3365.txt',
                'https://www.gutenberg.org/cache/epub/2506/pg2506.txt',
                'https://www.gutenberg.org/cache/epub/728/pg728.txt',
                'https://www.gutenberg.org/cache/epub/66257/pg66257.txt',
                'https://www.gutenberg.org/cache/epub/47060/pg47060.txt',
                'https://www.gutenberg.org/cache/epub/43469/pg43469.txt',
                'https://www.gutenberg.org/cache/epub/33608/pg33608.txt',
                'https://www.gutenberg.org/cache/epub/30108/pg30108.txt',
                'https://www.gutenberg.org/cache/epub/29993/pg29993.txt',
                'https://www.gutenberg.org/cache/epub/28763/pg28763.txt',
                'https://www.gutenberg.org/cache/epub/28305/pg28305.txt',
                'https://www.gutenberg.org/cache/epub/27880/pg27880.txt',
                'https://www.gutenberg.org/cache/epub/23030/pg23030.txt',
                'https://www.gutenberg.org/cache/epub/22519/pg22519.txt',
                'https://www.gutenberg.org/cache/epub/22297/pg22297.txt',
                'https://www.gutenberg.org/cache/epub/22219/pg22219.txt',
                'https://www.gutenberg.org/cache/epub/20403/pg20403.txt',
                'https://www.gutenberg.org/cache/epub/20225/pg20225.txt',
                'https://www.gutenberg.org/cache/epub/18605/pg18605.txt',
                'https://www.gutenberg.org/cache/epub/18565/pg18565.txt',
                'https://www.gutenberg.org/cache/epub/18555/pg18555.txt',
                'https://www.gutenberg.org/cache/epub/154/pg154.txt',
                'https://www.gutenberg.org/cache/epub/723/pg723.txt',
                'https://www.gutenberg.org/cache/epub/66584/pg66584.txt'
                ]

#Howell William Dean List: (I'm not considering the literature essays, just the literature books) - Indian Summer; Their silver wedding journey; 
# A hazard of new fortunes; Ragged Lady part1,2; The man of letters as a man of business; The landlord at Lion's head vol 1,2;
# Their weddng journey; The Sleeping Car, A farce; Emil Zola; Impressions and experiences; Years of my youth; A counterfeir presentment and the parlour car
# Bride roses; The quality of mercy; Poems, Imaginary Interviews; A likely story; Evening dress; Buying a horse;
# ; Christmas every day and other stories; The coast of bohemia; The flight of Pony Baker and A boy's town story; A fearful respondibility and other stories;
# The story of a play and A novel; A pair of patient lovers; A little Swiss Sojourn; A chance acquaintance; The rise of Silas Lapham;
# Henry James Jr; the World of Chance

creane_urls = ["https://www.gutenberg.org/cache/epub/43706/pg43706.txt",
                "https://www.gutenberg.org/cache/epub/39644/pg39644.txt",
                "https://www.gutenberg.org/cache/epub/33579/pg33579.txt",
                "https://www.gutenberg.org/cache/epub/31488/pg31488.txt",
                'https://www.gutenberg.org/cache/epub/31189/pg31189.txt',
                'https://www.gutenberg.org/cache/epub/19593/pg19593.txt',
                'https://www.gutenberg.org/cache/epub/9870/pg9870.txt',
                'https://www.gutenberg.org/cache/epub/7239/pg7239.txt',
                'https://www.gutenberg.org/cache/epub/2364/pg2364.txt',
                'https://www.gutenberg.org/cache/epub/463/pg463.txt',
                'https://www.gutenberg.org/cache/epub/447/pg447.txt',
                'https://www.gutenberg.org/cache/epub/45524/pg45524.txt'
                ]

# Stephen Crane list: Wounds in the rain and War stories; Whilomville Stories / Last words / The Little Regiment And Other Episodes of the American Civil War
# The Monster and Other Stories The Monster; The Blue Hotel; His New Mittens / The third violet / War is kind / Men, Women and boats /
# Active Service / The red badge of courage. An Episode of the American Civil War / Maggie: A girl of the streets / The open boat and other stories

twain_urls = ['https://www.gutenberg.org/cache/epub/1086/pg1086.txt',
            'https://www.gutenberg.org/cache/epub/1213/pg1213.txt',
            'https://www.gutenberg.org/cache/epub/3176/pg3176.txt',
            'https://www.gutenberg.org/cache/epub/3177/pg3177.txt',
            'https://www.gutenberg.org/cache/epub/2572/pg2572.txt',
            'https://www.gutenberg.org/cache/epub/3179/pg3179.txt',
            'https://www.gutenberg.org/cache/epub/5782/pg5782.txt',
            'https://www.gutenberg.org/cache/epub/5783/pg5783.txt',
            'https://www.gutenberg.org/cache/epub/5784/pg5784.txt',
            'https://www.gutenberg.org/cache/epub/5786/pg5786.txt',
            'https://www.gutenberg.org/cache/epub/5787/pg5787.txt',
            'https://www.gutenberg.org/cache/epub/5788/pg5788.txt',
            'https://www.gutenberg.org/cache/epub/5808/pg5808.txt',
            'https://www.gutenberg.org/cache/epub/5809/pg5809.txt',
            'https://www.gutenberg.org/cache/epub/5810/pg5810.txt',
            'https://www.gutenberg.org/cache/epub/5811/pg5811.txt',
            'https://www.gutenberg.org/cache/epub/5812/pg5812.txt',
            'https://www.gutenberg.org/cache/epub/5813/pg5813.txt',
            'https://www.gutenberg.org/cache/epub/5814/pg5814.txt',
            'https://www.gutenberg.org/cache/epub/5818/pg5818.txt',
            'https://www.gutenberg.org/cache/epub/5819/pg5819.txt',
            'https://www.gutenberg.org/cache/epub/5820/pg5820.txt',
            'https://www.gutenberg.org/cache/epub/5821/pg5821.txt',
            'https://www.gutenberg.org/cache/epub/5822/pg5822.txt',
            'https://www.gutenberg.org/cache/epub/5823/pg5823.txt',
            'https://www.gutenberg.org/cache/epub/5824/pg5824.txt',
            'https://www.gutenberg.org/cache/epub/5836/pg5836.txt',
            'https://www.gutenberg.org/cache/epub/5837/pg5837.txt',
            'https://www.gutenberg.org/cache/epub/5838/pg5838.txt',
            'https://www.gutenberg.org/cache/epub/5839/pg5839.txt',
            'https://www.gutenberg.org/cache/epub/5840/pg5840.txt',
            'https://www.gutenberg.org/cache/epub/5841/pg5841.txt',
            'https://www.gutenberg.org/cache/epub/5842/pg5842.txt',
            'https://www.gutenberg.org/cache/epub/7100/pg7100.txt',
            'https://www.gutenberg.org/cache/epub/7101/pg7101.txt',
            'https://www.gutenberg.org/cache/epub/7102/pg7102.txt',
            'https://www.gutenberg.org/cache/epub/7103/pg7103.txt',
            'https://www.gutenberg.org/cache/epub/7104/pg7104.txt',
            'https://www.gutenberg.org/cache/epub/7105/pg7105.txt',
            'https://www.gutenberg.org/cache/epub/7106/pg7106.txt',
            'https://www.gutenberg.org/cache/epub/7107/pg7107.txt',
            'https://www.gutenberg.org/cache/epub/7154/pg7154.txt',
            'https://www.gutenberg.org/cache/epub/7155/pg7155.txt',
            'https://www.gutenberg.org/cache/epub/7156/pg7156.txt',
            'https://www.gutenberg.org/cache/epub/7157/pg7157.txt',
            'https://www.gutenberg.org/cache/epub/7158/pg7158.txt',
            'https://www.gutenberg.org/cache/epub/7159/pg7159.txt',
            'https://www.gutenberg.org/cache/epub/7160/pg7160.txt',
            'https://www.gutenberg.org/cache/epub/7161/pg7161.txt',
            'https://www.gutenberg.org/cache/epub/7162/pg7162.txt',
            'https://www.gutenberg.org/cache/epub/7193/pg7193.txt',
            'https://www.gutenberg.org/cache/epub/7194/pg7194.txt',
            'https://www.gutenberg.org/cache/epub/7195/pg7195.txt',
            'https://www.gutenberg.org/cache/epub/7196/pg7196.txt',
            'https://www.gutenberg.org/cache/epub/7197/pg7197.txt',
            'https://www.gutenberg.org/cache/epub/7198/pg7198.txt',
            'https://www.gutenberg.org/cache/epub/7199/pg7199.txt',
            'https://www.gutenberg.org/cache/epub/7200/pg7200.txt',
            'https://www.gutenberg.org/cache/epub/7242/pg7242.txt',
            'https://www.gutenberg.org/cache/epub/7243/pg7243.txt',
            'https://www.gutenberg.org/cache/epub/7244/pg7244.txt',
            'https://www.gutenberg.org/cache/epub/7245/pg7245.txt',
            'https://www.gutenberg.org/cache/epub/7246/pg7246.txt',
            'https://www.gutenberg.org/cache/epub/7247/pg7247.txt',
            'https://www.gutenberg.org/cache/epub/7248/pg7248.txt',
            'https://www.gutenberg.org/cache/epub/7249/pg7249.txt',
            'https://www.gutenberg.org/cache/epub/7250/pg7250.txt',
            'https://www.gutenberg.org/cache/epub/8471/pg8471.txt',
            'https://www.gutenberg.org/cache/epub/8472/pg8472.txt',
            'https://www.gutenberg.org/cache/epub/8473/pg8473.txt',
            'https://www.gutenberg.org/cache/epub/8474/pg8474.txt',
            'https://www.gutenberg.org/cache/epub/8475/pg8475.txt',
            'https://www.gutenberg.org/cache/epub/8476/pg8476.txt',
            'https://www.gutenberg.org/cache/epub/8477/pg8477.txt',
            'https://www.gutenberg.org/cache/epub/8478/pg8478.txt',
            'https://www.gutenberg.org/cache/epub/8479/pg8479.txt',
            'https://www.gutenberg.org/cache/epub/8480/pg8480.txt',
            'https://www.gutenberg.org/cache/epub/8481/pg8481.txt',
            'https://www.gutenberg.org/cache/epub/8482/pg8482.txt',
            'https://www.gutenberg.org/cache/epub/8526/pg8526.txt',
            'https://www.gutenberg.org/cache/epub/8527/pg8527.txt',
            'https://www.gutenberg.org/cache/epub/8528/pg8528.txt'
            ]
# Mark Twain list: A horse's Tale / The man that corrupted Hadleyburg / The innocents abroad / Roughing it / On the decay of the art of lying
# The American claimant / A tramp abroad / Following the equatore: a journey around the world / The Gilden age / Sketches new ad old / 
#Sketches New and Old / Adventures of Huckleberry Finn / The Prince and the pauper / The adventures of Tom Sawyer / A Connecticut Yankee in King Arthur's Court
# Life on the Mississippi / Eve's diary

jacobs_urls = ["https://www.gutenberg.org/cache/epub/11030/pg11030.txt"]

#Jacobs: Incidents in the Life of a Slave Girl

whitman_urls = ["https://www.gutenberg.org/cache/epub/8388/pg8388.txt",
                "https://www.gutenberg.org/cache/epub/8813/pg8813.txt"]
#Whitman: all the Poems and all the Prose

irving_urls = ["https://www.gutenberg.org/cache/epub/8571/pg8571.txt",
                'https://www.gutenberg.org/cache/epub/7948/pg7948.txt',
                'https://www.gutenberg.org/cache/epub/1850/pg1850.txt',
                'https://www.gutenberg.org/cache/epub/14228/pg14228.txt',
                'https://www.gutenberg.org/cache/epub/13042/pg13042.txt',
                'https://www.gutenberg.org/cache/epub/41/pg41.txt',
                'https://www.gutenberg.org/cache/epub/7994/pg7994.txt',
                'https://www.gutenberg.org/cache/epub/7993/pg7993.txt',
                ]

#Irving list: Wolfert's Roost and Miscellanies / Abbotsford and Newstead Abbey / Old Christmas / Bracebridge Hall / Knickerbocker's History of New York, Complete
# The Legend of Sleepy Hollow / The Crayon Papers / Oliver Goldsmith

bryant_urls = ["https://www.gutenberg.org/cache/epub/16341/pg16341.txt"]

#Bryant list: all the pomes

longfellow_urls = ["https://www.gutenberg.org/cache/epub/13830/pg13830.txt",
                    "https://www.gutenberg.org/cache/epub/10490/pg10490.txt",
                    "https://www.gutenberg.org/cache/epub/25153/pg25153.txt",
                    "https://www.gutenberg.org/cache/epub/30795/pg30795.txt",
                    "https://www.gutenberg.org/cache/epub/44398/pg44398.txt",
                    "https://www.gutenberg.org/cache/epub/2039/pg2039.txt", 
                    "https://www.gutenberg.org/cache/epub/5436/pg5436.txt"
                    ]

# Longfellow list: The wreck of the hesperus / The golden legend / Tales of a Wayside Inn / The song of Hiawatha, an epic poem / Poems of slavery 
# Evangeline. A tale of acadie / Hyperion 

london_urls = ["https://www.gutenberg.org/cache/epub/12336/pg12336.txt",
                "https://www.gutenberg.org/cache/epub/11051/pg11051.txt",
                'https://www.gutenberg.org/cache/epub/14449/pg14449.txt',
                'https://www.gutenberg.org/cache/epub/14654/pg14654.txt',
                'https://www.gutenberg.org/cache/epub/14658/pg14658.txt',
                'https://www.gutenberg.org/cache/epub/215/pg215.txt',
                'https://www.gutenberg.org/cache/epub/18062/pg18062.txt',
                'https://www.gutenberg.org/cache/epub/21936/pg21936.txt',
                'https://www.gutenberg.org/files/21970/21970-0.txt',
                'https://www.gutenberg.org/files/21971/21971-0.txt',
                'https://www.gutenberg.org/cache/epub/22104/pg22104.txt',
                'https://www.gutenberg.org/cache/epub/28693/pg28693.txt',
                'https://www.gutenberg.org/cache/epub/48474/pg48474.txt',
                'https://www.gutenberg.org/files/54068/54068-0.txt',
                'https://www.gutenberg.org/cache/epub/55948/pg55948.txt',
                'https://www.gutenberg.org/cache/epub/16257/pg16257.txt',
                'https://www.gutenberg.org/cache/epub/318/pg318.txt',
                'https://www.gutenberg.org/cache/epub/710/pg710.txt',
                'https://www.gutenberg.org/cache/epub/746/pg746.txt',
                'https://www.gutenberg.org/cache/epub/910/pg910.txt',
                'https://www.gutenberg.org/cache/epub/1074/pg1074.txt',
                'https://www.gutenberg.org/cache/epub/1089/pg1089.txt',
                'https://www.gutenberg.org/cache/epub/1096/pg1096.txt',
                'https://www.gutenberg.org/cache/epub/1160/pg1160.txt',
                'https://www.gutenberg.org/cache/epub/1161/pg1161.txt',
                'https://www.gutenberg.org/cache/epub/1163/pg1163.txt',
                'https://www.gutenberg.org/cache/epub/1187/pg1187.txt',
                'https://www.gutenberg.org/cache/epub/1596/pg1596.txt',
                'https://www.gutenberg.org/cache/epub/1655/pg1655.txt',
                'https://www.gutenberg.org/cache/epub/1669/pg1669.txt',
                'https://www.gutenberg.org/cache/epub/1730/pg1730.txt',
                'https://www.gutenberg.org/cache/epub/2152/pg2152.txt',
                'https://www.gutenberg.org/cache/epub/2377/pg2377.txt',
                'https://www.gutenberg.org/cache/epub/2416/pg2416.txt',
                'https://www.gutenberg.org/cache/epub/4953/pg4953.txt',
                'https://www.gutenberg.org/cache/epub/6455/pg6455.txt',
                'https://www.gutenberg.org/cache/epub/10736/pg10736.txt'
,                ]

# Jack London list: Brown Wolf and Other Jack London Stories / The cruise of the dazzler / Dutch courage and other stories / A daughter of the snow
# The road / The call of the wind / Stories of the ships and the sea / Theft. A play in four acts / The scarlet plague / A son of the sun 
#  The acorn-planter / Tales of the fish patrol / Scorn of Women. A play in 3 acts / Hearts of 3 / The Abysmal brute / The turtles of tasman / 
# John Barleycorn / Love and Life and other stories /  Burning daylight / White fang / The sea-wolf / Moon-face and other stories 
# The faith of men / The game / Jerry of the islands / Adventure / War of the classes / Smoke Bellew / The god of his fathers
# The human drift / Michael, brother of Jerry / Island Tales. On the Makaloa Mat / The son of the wolf / The house of pride and other tales of Hawaii
# Revolution and other essays / The little lady of the big house / Children of the frost

norris_urls = ['https://www.gutenberg.org/files/48620/48620-0.txt',
                'https://www.gutenberg.org/files/165/165-0.txt',
                'https://www.gutenberg.org/cache/epub/26026/pg26026.txt',
                'https://www.gutenberg.org/cache/epub/16096/pg16096.txt',
                'https://www.gutenberg.org/cache/epub/14712/pg14712.txt',
                'https://www.gutenberg.org/cache/epub/9905/pg9905.txt',
                'https://www.gutenberg.org/cache/epub/4382/pg4382.txt',
                'https://www.gutenberg.org/cache/epub/401/pg401.txt',
                'https://www.gutenberg.org/files/321/321-0.txt',
                'https://www.gutenberg.org/files/268/268-0.txt'
                ]

# Frank Norris list: The Third Circle / McTeague: A Story of San Francisco / The Surrender of Santiago / A Man's Woman / Vandover and the Brute
# A Deal in Wheat and Other Stories / The Pit: A Story of Chicago / Blix / Moran of the Lady Letty / The Octopus : A Story of California

douglass_urls = ["https://www.gutenberg.org/cache/epub/202/pg202.txt",
                'https://www.gutenberg.org/cache/epub/34915/pg34915.txt', 
                'https://www.gutenberg.org/files/59116/59116-0.txt',
                'https://www.gutenberg.org/cache/epub/67919/pg67919.txt',
                'https://www.gutenberg.org/files/23/23-0.txt'
                ]
# Frederick Douglass list: My bondage and my freedom / Abolition Fanaticism in New York / Why is the Negro Lynched? / Three addresses on the relations subsisting between the white and colored people
# Narrative of the life of Frederick Douglass: an American slave

hemingway_urls = ["https://www.gutenberg.org/cache/epub/69683/pg69683.txt",
                    'https://www.gutenberg.org/cache/epub/67138/pg67138.txt',
                    'https://www.gutenberg.org/files/61085/61085-0.txt',
                    'https://www.gutenberg.org/files/59603/59603-0.txt'
                    ]
#Hemingway list: Men without women / The sun also rises / In our time / 3 stories and 10 poems 

hurston_hughes_urls = ['https://www.gutenberg.org/files/19435/19435-0.txt']

# Hurston-Hughes List: The Mule-Bone: A Comedy of Negro Life in Three Acts

hurston_urls = ['https://www.gutenberg.org/cache/epub/22146/pg22146.txt',
                'https://www.gutenberg.org/cache/epub/17187/pg17187.txt',
                'https://www.gutenberg.org/cache/epub/15902/pg15902.txt'
                ]
            
#Hurston list: 	Poker! / Three Plays Lawing and Jawing; Forty Yards; Woofing / De Turkey and De Law A Comedy in Three Acts

fitzgerald_urls = ['https://www.gutenberg.org/cache/epub/68229/pg68229.txt',
                    'https://www.gutenberg.org/files/805/805-0.txt',
                    'https://www.gutenberg.org/cache/epub/4368/pg4368.txt',
                    'https://www.gutenberg.org/files/6695/6695-0.txt',
                    'https://www.gutenberg.org/files/9830/9830-0.txt',
                    'https://www.gutenberg.org/files/60962/60962-0.txt',
                    'https://www.gutenberg.org/cache/epub/64317/pg64317.txt'
                    ]
#Fitzgerald list: This Side of Paradise / Flappers and Philosophers / Tales of the Jazz Age / The Beautiful and Damned 
#The Vegetable; or, From President to Postman / The Great Gatsby / All the Sad Young Men

vonnegut_urls = ['https://www.gutenberg.org/cache/epub/30240/pg30240.txt',
                'https://www.gutenberg.org/cache/epub/21279/pg21279.txt'
                ]

# Vonnegut list: 2 B R 0 2 B / The Big Trip Up Yonder

dick_urls = ['https://www.gutenberg.org/cache/epub/28554/pg28554.txt',
            'https://www.gutenberg.org/cache/epub/28644/pg28644.txt',
            'https://www.gutenberg.org/cache/epub/28698/pg28698.txt',
            'https://www.gutenberg.org/cache/epub/28767/pg28767.txt',
            'https://www.gutenberg.org/cache/epub/29132/pg29132.txt',
            'https://www.gutenberg.org/cache/epub/30255/pg30255.txt',
            'https://www.gutenberg.org/cache/epub/31516/pg31516.txt',
            'https://www.gutenberg.org/cache/epub/32032/pg32032.txt',
            'https://www.gutenberg.org/cache/epub/32154/pg32154.txt',
            'https://www.gutenberg.org/cache/epub/32522/pg32522.txt',
            'https://www.gutenberg.org/cache/epub/32832/pg32832.txt',
            'https://www.gutenberg.org/cache/epub/40964/pg40964.txt',
            'https://www.gutenberg.org/cache/epub/41562/pg41562.txt'
]

# Dick list: The Hanging Stranger / Tony and the Beetles / Piper in the Woods / Mr. Spaceship / The Variable Man / Second Variety
# 	The Eyes Have It / The Skull / The Gun / The Defenders / The Crystal Crypt / Beyond the Door / Beyond Lies the Wub

miller_urls = ['https://www.gutenberg.org/files/50294/50294-0.txt',
                'https://www.gutenberg.org/files/35563/35563-0.txt'
                ]

#Miller list: Indian Creek Massacre and Captivity of Hall Girls / The Clergyman’s Hand-book of Law

faulkner = 'C:/Users/renato/Desktop/CL/CLProj/TextsCorpus/Faulkner_CollectedStories'

lee = 'C:/Users/renato/Desktop/CL/CLProj/TextsCorpus/Lee_To kill a mockingbird'

plath_url = ['https://www.gutenberg.ca/ebooks/plaths-belljar/plaths-belljar-00-h.html'] 

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
