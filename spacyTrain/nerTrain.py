import spacy
from spacy.pipeline import EntityRecognizer
from spacy.gold import GoldParse
from spacy.tagger import Tagger
import random

model_name = 'en'
entity_label = 'GUI1'
output_directory = 'C:/Users/dusalk/Documents/python_projects/new/nlp_nltk/data/en_gui1'
train_data = [
    (u'The user should be connected to a coordinator in the sites per user window',
    [(53, 58, 'B-GUI1'),(59,62,'I-GUI1'),(63,67,'L-GUI1')]),
    (u'The customer should have a record in the customer window',
    [(41, 49, 'GUI1')]),
    (u'Open the sales quotation window',
    [(9, 14, 'B-GUI1'),(15,24,'L-GUI1')]),
    (u'and for internal customers this can be done in the Site to Site Supply Chain Parameters window',
    [(51, 55, 'B-GUI1'),(56,58,'I-GUI1'),(59,63,'I-GUI1'),(64,70,'I-GUI1'),(71,76,'I-GUI1'),(77,87,'L-GUI1')])
]

def train_ner(nlp, train_data, output_dir):
    # Add new words to vocab
    for raw_text, _ in train_data:
        doc = nlp.make_doc(raw_text)
        for word in doc:
            _ = nlp.vocab[word.orth]

    for itn in range(20):
        random.shuffle(train_data)
        for raw_text, entity_offsets in train_data:
            doc = nlp.make_doc(raw_text)
            gold = GoldParse(doc, entities=entity_offsets)
            nlp.tagger(doc)
            loss = nlp.entity.update(doc, gold)
    nlp.end_training()
    nlp.save_to_directory(output_dir)

nlp = spacy.load(model_name)
nlp.entity.add_label(entity_label)
ner = train_ner(nlp, train_data, output_directory)

