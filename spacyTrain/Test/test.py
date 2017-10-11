from spacy.vocab import Vocab
from spacy.pipeline import EntityRecognizer
from spacy.tokens import Doc

vocab = Vocab()
entity = EntityRecognizer(vocab, entity_types=['PERSON', 'LOC'])

doc = Doc(vocab, words=['Who', 'is', 'Shaka', 'Khan', '?'])
entity.update(doc, ['O', 'O', 'B-PERSON', 'L-PERSON', 'O'])

entity.model.end_training()
