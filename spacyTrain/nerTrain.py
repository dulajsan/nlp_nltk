import spacy
from spacy.pipeline import EntityRecognizer
from spacy.gold import GoldParse
from spacy.tagger import Tagger
import random

model_name = 'en'
entity_label1 = 'GUI1'
entity_label2 = 'GUI2'

#trained model state saving directory
output_directory = 'C:/Users/dusalk/Documents/python_projects/new/nlp_nltk/data/en_gui'
#train data by manually tagging
train_data = [
    (u'The user should be connected to a coordinator in the sites per user window',
    [(53, 67, 'GUI1')]),
    (u'The customer should have a record in the customer window',
    [(41, 49, 'GUI1')]),
    (u'Open the sales quotation window',
    [(9, 24, 'GUI1')]),
    (u'and for internal customers this can be done in the Site to Site Supply Chain Parameters window',
    [(51, 87, 'GUI1')]),
    (u'The quotation Lines tab is used to specify the parts and quantities that the customer wants to order',
     [(4,19,'GUI1')]),
    (u'Replacement parts are entered in the Sales Part/Misc Part Info, Non-Inventory Sales Part/Misc Part Info or Package Part/Misc Part Info tab windows, depending on the type of part that is to be replaced.',
     [(38,134,'GUI1')]),
    (u'Substitute sales parts must be connected to the appropriate sales parts in the Alternate Sales Parts Base Data window.',
     [(79,110,'GUI1')]),
    (u'If the customer has the Receive Pack Size Charge/Discount check box selected in the Customer/Order/General tab',
     [(84,107,'GUI1')]),
    (u'Either specify the sales part number, service part number, or package part number directly in the Sales Part No field or search for it by using the List of Values',
     [(98,111,'GUI2')]),
    (u'Indicate the quantity of requested parts in the Sales Quantity field.',
     [(48,62,'GUI2')]),
    (u'You can select an input UoM from the Input UoM list',
     [(37, 46,'GUI2')]),
    (u'If the customer has the Receive Pack Size Charge/Discount check box selected in the Customer/Order/General tab',
     [(24,57,'GUI2'),(84,106,'GUI1')])

]

# def newGoldner(abc):
#     a = abc
#     b = [str(t) for t in a]
#     lst = []
#
#     for q in b:
#         if q[0] == 'U':
#             lst.append(q[2:])
#         else:
#             lst.append(q)
#
#     return lst


#train function
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
#add new entity type
nlp.entity.add_label(entity_label1)
nlp.entity.add_label(entity_label2)


ner = train_ner(nlp, train_data, output_directory)

