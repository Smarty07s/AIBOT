import nltk
from nltk.tokenize import sent_tokenize,word_tokenize


query = str(input("Query: "))

sent_tok = sent_tokenize(query)
word_tok = word_tokenize(query)


print(sent_tok,word_tok)
