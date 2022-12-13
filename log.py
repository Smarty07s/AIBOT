from functions import abcd,json,sent_tokenize,word_tokenize


text = input('Enter: ')

f = []
for l in ['corp/raw/doc0.txt','corp/raw/doc1.txt','corp/raw/doc2.txt']:
    d = open(l,'r')
    r = word_tokenize(d.read())
    f.append(r)
    
val = abcd().tfidf(text,f)

# jfilew = open('corp/json/data.json','w')
jfiler = open('corp/json/data.json','r').read()
print(jfiler)

open('corp/json/data.json','r').close()

data = json.loads(jfiler)

data[text] = val

jstring = json.dumps(data)

jfilew = open('corp/json/data.json','w')
jfilew.write(jstring)
jfilew.close()
