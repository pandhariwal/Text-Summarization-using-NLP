def optimize(text):

    i = input('Enter the compression level (High/Medium/low):')
    if i.lower() == 'high':
        x = 3
    if i.lower() == 'medium':
        x = 5
    if i.lower() == 'low':
        x = 8

    y = ((len(text)*x*10)/100)

    r = text.find('.', int(y), len(text))

    print(text[0:int(r)+1])
#=======================================================================================================================


def common(article_text):
    import re
    import nltk

    # Removing Square Brackets and Extra Spaces
    article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
    article_text = re.sub(r'\s+', ' ', article_text)

    # Removing special characters and digits
    formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text)
    formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)

    sentence_list = nltk.sent_tokenize(article_text)

    print("Sentence list as follows:")
    print(sentence_list)
    print("===================================================")

    stopwords = nltk.corpus.stopwords.words('english')

    word_frequencies = {}
    for word in nltk.word_tokenize(formatted_article_text):
        if word not in stopwords:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1

    print("Word frequencies is a s follows:")
    print(word_frequencies)
    print("====================================================")

    maximum_frequncy = max(word_frequencies.values())

    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word] / maximum_frequncy)

    sentence_scores = {}
    for sent in sentence_list:
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_frequencies.keys():
                if len(sent.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word]
                    else:
                        sentence_scores[sent] += word_frequencies[word]

    print("Sentence scores are as follows:")
    print(sentence_scores)
    print("===============================================")

    import heapq
    summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)

    summary = ' '.join(summary_sentences)
    print("The Summary is:\n")
    print(summary)

    print("=========================================================")

    print("The optimized text is as follows:\n")
    optimize(summary)


#=======================================================================================================================


#======================================================one main=========================================================

def onemain(text):
    article_text = text
    common(article_text)

#=======================================================two main========================================================


def twomain(val1):
    import bs4 as bs
    import urllib.request

    scraped_data = urllib.request.urlopen(val1)
    article = scraped_data.read()

    parsed_article = bs.BeautifulSoup(article, "html.parser")

    paragraphs = parsed_article.find_all('p')

    article_text = ""

    for p in paragraphs:
        article_text += p.text

    common(article_text)

#======================================================three main=======================================================


def threemain():

    import speech_recognition as sr
    import requests

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=3, phrase_time_limit=20)
        print("Time over, Thanks")
        file1 = open("myfile.txt", "w")
        tex = r.recognize_google(audio)
        dat = {'text': tex}
        r = requests.post("http://bark.phon.ioc.ee/punctuator", data=dat)
        aarush = r.text
        file1.writelines(aarush)
        print("The input text is as follows:")
        print(aarush)
        print("===================================================================")
        file1.close()

    file1 = open("myfile.txt", "r+")
    text = file1.read()
    common(text)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


print("Make a choice: 1. Normal Text. 2. Website. 3. Audio Input.")
#========================================================Choice Normal Text=============================================


def one():
    val1 = input("Enter the Normal text\n")
    print("U hve entered :" + val1)
    onemain(val1)

#========================================================Choice Website=================================================


def two():
    val1 = input("Enter the website url (including https://)\n")
    print("U hve entered :" + val1)
    twomain(val1)


#========================================================Choice Audio Input=============================================


def three():
    print("You have chosen audio input\n")
    threemain()


#-------------------------------------------------------------switch----------------------------------------------------


def switch_func(value, x):
    return {
        '1': lambda x: one(),
        '2': lambda x: two(),
        '3': lambda x: three(),

    }.get(value)(x)

inp = input('Enter the Choice : ')
switch_func(inp, 2)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

