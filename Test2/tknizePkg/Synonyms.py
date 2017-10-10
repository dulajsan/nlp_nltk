from nltk.corpus import wordnet
syn = wordnet.synsets('cookbook')[0]
lemmas = syn.lemmas
len(lemmas)
#2
lemmas[0].name
'cookbook'
lemmas[1].name
'cookery_book'
lemmas[0].synset == lemmas[1].synset
True