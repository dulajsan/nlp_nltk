import spacy
from spacy.pipeline import EntityRecognizer
from spacy.gold import GoldParse
from spacy.tagger import Tagger
import random

model_name = 'en'
entity_label = 'GUI2'
output_directory = 'C:/Users/dusalk/Documents/python_projects/new/nlp_nltk/data/en_gui2'
train_data = [
    (u'If the customer order is created in Released status, the value for the Release for Material Planning check box will be selected',
    [(71, 78, 'GUI2'),(79,82,'I-GUI2'),(83,91,'I-GUI2'),(92,100,'GUI2')]),
    (u'Optionally, change the main competitor by unselecting and selecting the check box in the Main Competitor field.',
    [(89, 93, 'GUI2'),(94,104,'GUI2')])

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

