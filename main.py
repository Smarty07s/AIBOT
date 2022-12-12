import nltk
import os
import json
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

query = (str(input("Query: "))).lower()

sent_seg = sent_tokenize(query)
word_tok = word_tokenize(query)
# print(stopwords.words('english'))

b = 2
for i in range(b):
    if os.path.exists(f'corp/raw/doc{i}.txt') == True:
        print(True)
        b += 1
    elif os.path.exists(f'corp/raw/doc{i}.txt') == False:
        print(False)
        document = open(f'corp/raw/doc{i}.txt', 'w')
        document.write(query)
        document.close()
        document = open(f'corp/sent_seg/doc{i}.txt', 'w')
        document.write(str(sent_seg))
        document.close()
        document = open(f'corp/word_tok/doc{i}.txt', 'w')
        document.write(str(word_tok))
        break



