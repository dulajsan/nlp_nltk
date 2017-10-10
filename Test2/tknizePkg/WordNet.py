#this is like  a dictionary
from nltk.corpus import wordnet
syn = wordnet.synsets('cookbook')[0]
syn.name
#'cookbook.n.01'
print(syn.definition)
#'a book of recipes and cooking directions'