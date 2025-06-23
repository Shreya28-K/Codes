import nltk 
#nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
print("I love touse Chat gbt for song suggestion")
sample_text="I love Gen AI"
list_test=word_tokenize(sample_text.lower())
print("Tokenization = \n")
print(list_test)

unigram=list(ngrams(list_test,1))
print("Unigram = \n")
print(unigram)

bigram=list(ngrams(list_test,2))
print("Bigram = \n")
print(bigram)
trigram=list(ngrams(list_test,3))
print("Trigram = \n")
print(trigram)

