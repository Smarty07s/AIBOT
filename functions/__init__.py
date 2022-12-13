import time
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

            tfidf = log(b)/e

        return tfidf
            


d = open('functions/doc0.txt','r')
r = word_tokenize(d.read())
print(abcd().tfidf('and',[r,]))

time.sleep(6.0)