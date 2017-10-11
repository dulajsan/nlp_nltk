import spacy
from spacy.gold import GoldParse

nlp = spacy.load('en')
doc = nlp.make_doc(u'Facebook released React in 2014')
gold = GoldParse(doc, entities=['U-ORG', 'O', 'O', 'O', 'U-DATE'])
nlp.entity.update(doc, gold)
