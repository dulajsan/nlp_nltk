import spacy                           # See "Installing spaCy"
nlp = spacy.load('en')                 # You are here.
doc = nlp(u'Hello, spacy!')            # See "Using the pipeline"
print([(w.text, w.ent_type_) for w in doc])
