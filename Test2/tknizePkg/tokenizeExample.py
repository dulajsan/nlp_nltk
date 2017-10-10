import nltk
from nltk.tokenize import word_tokenize
word_tokenize('Hello World.')
['Hello', 'World', '.']

#same

from nltk.tokenize import TreebankWordTokenizer
tokenizer = TreebankWordTokenizer()
tokenizer.tokenize('Hello World.')
['Hello', 'World', '.']