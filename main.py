import nltk
import os
from nltk.tokenize import sent_tokenize,word_tokenize
from  nltk.corpus import stopwords

query = (str(input("Query: "))).lower()

sent_tok = sent_tokenize(query)
word_tok = word_tokenize(query)
# print(stopwords.words('english'))

print(os.system('notepad'))
 
