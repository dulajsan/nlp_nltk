import nltk
from nltk import word_tokenize

patterns = [
    (r'.*ing$', 'VBG'),               # gerunds
    (r'.*ed$', 'VBD'),                # simple past
    (r'.*es$', 'VBZ'),                # 3rd singular present
    (r'.*ould$', 'MD'),               # modals
    (r'.*window$', 'WINDOW'),
    (r'.*\'s$', 'NN$'),               # possessive nouns
    (r'.*s$', 'NNS'),                 # plural nouns
    (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),  # cardinal numbers
    (r'.*', 'NN')                     # nouns (default)
]



raw = 'Click the abc window'
tokens = word_tokenize(raw)
default_tagger = nltk.DefaultTagger('NN')
regexp_tagger = nltk.RegexpTagger(patterns)
#tagers=default_tagger.tag(tokens)
tagers=regexp_tagger.tag(tokens)
print(tagers)
