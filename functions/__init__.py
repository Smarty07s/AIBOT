def createf(filename , data):
    with open(filename,'w'):
        f = open(filename,'w')
        f.write(data)
        f.close()

class abcd():
    def __init__(self) -> None:
        return None
    
    def tfidf(self,word,documents):
        for i in documents:
            d = open(i,'r')
            r = list(d.read())
            for a in r:
                if word in r:
                    print(word)
                print(a)

print(abcd().tfidf('and',['doc0.txt']))