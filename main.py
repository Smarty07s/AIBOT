import nltk
from nltk.tokenize import sent_tokenize


query = str(input("Query: "))

senttok = sent_tokenize(query)

print(senttok)
