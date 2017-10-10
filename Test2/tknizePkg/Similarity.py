from nltk.corpus import wordnet
cb = wordnet.synset('cookbook.n.01')
ib = wordnet.synset('instruction_book.n.01')
cb.wup_similarity(ib)
#0.91666666666666663

