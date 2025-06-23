import nltk
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize
text = 'I love Generative AI!'
tokens = word_tokenize(text)
print('Tokens:', tokens)