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
            
f = []
for l in ['corp/raw/doc0.txt','corp/raw/doc1.txt','corp/raw/doc2.txt']:
    d = open(l,'r')
    r = word_tokenize(d.read())
    f.append(r)
print(abcd().tfidf('and',f))

