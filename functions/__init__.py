import time
import json
from nltk.tokenize import sent_tokenize,word_tokenize
from math import log



def createf(filename , data):
    with open(filename,'w'):
        f = open(filename,'w')
        f.write(data)
        f.close()

class abcd():
    def __init__(self) -> None:
        pass
    
    def tfidf(self,word,text):
        b = 0
        e = len(text)
        for c in text:
            for a in c:

                if word == a:
                    ret = True
                else:
                    ret = False
                if ret == True:
                    b = b+1

            tfidf = b/e

        return tfidf






