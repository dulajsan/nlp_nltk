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
     [(24,57,'GUI2'),(84,106,'GUI1')]),
    (u'Open the Material Requisition window and create a new record.',
     [(9,29,'GUI1')]),
    (u'You have the option to enter an internal destination. Enter either the ID in the Internal Destination ID field or write a description directly in the Description field. If you have entered an internal destination ID you can still change the description for this specific material requisition',
     [(81,104,'GUI2'),(150,161,'GUI2')]),
    (u'Project manual connections to the material requisition lines must have been made available on the Project /Manual Connections tab',
     [(98,125,"GUI1")]),
    (u'The Project Navigator/Connections tab and the Project/Demand/Material Requisition Line tab will display details of the material requisition line connected to the project activity',
     [(4,33,"GUI1"),(46,86,"GUI1")]),
    (u'Open the Material Requisition window, and search for the relevant material requisition.',
     [(9,29,"GUI1")]),
    (u'The Connect to Activity dialog box opens',
     [(4,23,"GUI1")]),
    (u'You can continue to specify the criteria for the activity you want to select by clicking on the Project ID, Sub Project ID, and Activity ID fields',
     [(96,139,"GUI2")]),
    (u'Alternatively, you can enter the activity sequence in the Activity Sequence field',
     [(58,75,"GUI2")]),
    (u'You can obtain the activity sequence from the Project Navigator/Activity/Details tab',
     ([(46,80,"GUI1")])),
    (u'This activity is used to disconnect a manually connected material requisition line from the project activity. You can perform this activity from the Material Requisition window itself',
     [(149,169,"GUI1")]),
    (u'The material requisition line will no longer appear as a connection on the Project Navigator/Connections tab.',
     [(75,104,"GUI1")]),
    (u'Open the Material Requisition window, and search for the relevant material requisition',
     [(9,29,"GUI1")]),
    (u'Open the Material Requisition window and populate or query for the appropriate material requisition.',
     [(9,29,"GUI1")]),
    (u'The parts are reserved in stock and the order line status is updated from Released to Reserved. You can see the quantity of parts reserved in the Qty Reserved field.',
     [(146,158,"GUI2")]),
    (u'The Rem Qty to Res field of the Manual Reservation dialog box shows how many parts remain to be reserved',
     [(4,19,"GUI2"),(32,50,"GUI1")]),
    (u'You can also remove a reservation by entering a negative quantity in the Reserve Qty field.',
     [(73,84,"GUI2")]),
    (u'The parts are reserved and the requisition line status is updated from Released to Reserved. You can see how many parts are reserved in the Qty Reserved column.',
     [(140,152,"GUI2")]),
    (u'Select the Reserve Manually function in the Operations menu. The Manual Reservation dialog box opens up.',
     [(65,84,"GUI1")]),
    (u'In the line for the proper inventory location, enter the quantity that you want to reserve in the Reserve Qty field.',
     [(98,110,"GUI2")]),
    (u'You can see the quantity to be reserved in the Rem Qty to Res field.',
     [(47,61,"GUI2")])

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

