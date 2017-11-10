#same data added after line 120

import spacy
from spacy.pipeline import EntityRecognizer
from spacy.gold import GoldParse
from spacy.tagger import Tagger
import random

model_name = 'en'
entity_label1 = 'GUI1'
entity_label2 = 'GUI2'
entity_label3 = 'ACTION'

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
     [(47,61,"GUI2")]),
    (u'Open the Serial Parts window. You can also perform this procedure from the Serial Part window.',
     [(75,86,"GUI1")]),
    (u'In the Condition Code, Cond Limit Description, and Standard Value fields',
     [(7,45,"GUI2"),(51,65,"GUI2")]),
    (u'Click the Task Cards tab and create a new record',
     [(10,20,"GUI1")]),
    (u'Click the Task Cards tab and then click the Task Cards sub tab',
     [(10,20,"GUI1"),(44,54,"GUI1")]),
    (u'In the Task Card ID field',
     [(7,19,"GUI2")]),
    (u'revert to the default value by selecting the Reset Serial Base Number check box.',
     [(45,68,"GUI2")]),
    (u'Click OK.',
     [(6,8,"ACTION")]),
    (u'If needed, modify the Serial Base Number ',
     [(22,40,"ACTION")]),
    (u'Right-click and click Manage Serial Number Generation',
     [(22,53,"ACTION")]),
    (u'When serial parts are defined, the Life Limited field does not display any value',
     [(35,53,"GUI2")]),
    (u'Use the BP Links portlet for maintaining all links to cubes and scorecards you deal with on a regular ',
     [(8,16,"GUI1")]),
    (u'Open the Document Info page to get detailed information on the document',
     [(9,22,"GUI1")]),
    (u'Enter all required data in the Copy Parts to Site dialog box',
     [(32,49,"GUI1")]),
    (u'On the Navigate menu',
     [(7,15,"GUI2")]),
    (u'You can enter new values for the proposed schedule on the Proposed Schedule tab ',
     [(58,75,"GUI1")]),
    (u'the work load for the work centers can be compared on the Schedule Analysis and Load Analysis tabs',
     [(58,75,"GUI1"),(80,93,"GUI1")]),
    (u'Enter a description in the Quotation Desc field.',
     [(27,41,"GUI2")]),
    (u'enter suitable dates in the Request Receipt Date and Price Effective Date fields.',
     [(28,48,"GUI2"),(53,73,"GUI2")]),
    (u' Engineering parts can also be inserted in the Engineering Parts window',
     [(46,63,"GUI1")]),
    (u'Use the calculate characteristics menu option to calculate the characteristics for a part.',
     [(8,33,"GUI2")]),
    (u'The user should be connected to a coordinator in the sites per user window',
     [(53, 67, 'GUI1')]),
    (u'The customer should have a record in the customer window',
     [(41, 49, 'GUI1')]),
    (u'Open the sales quotation window',
     [(9, 24, 'GUI1')]),
    (u'and for internal customers this can be done in the site to site supply chain parameters window',
     [(51, 87, 'GUI1')]),
    (u'The quotation lines tab is used to specify the parts and quantities that the customer wants to order',
     [(4, 19, 'GUI1')]),
    (
    u'Replacement parts are entered in the sales part/misc part info, non-inventory sales part/misc part info or Package Part/Misc Part Info tab windows, depending on the type of part that is to be replaced.',
    [(38, 134, 'GUI1')]),
    (
    u'Substitute sales parts must be connected to the appropriate sales parts in the alternate sales parts base data window.',
    [(79, 110, 'GUI1')]),
    (u'If the customer has the receive pack size charge/discount check box selected in the customer/order/general tab',
     [(84, 107, 'GUI1')]),
    (
    u'Either specify the sales part number, service part number, or package part number directly in the sales part no field or search for it by using the List of Values',
    [(98, 111, 'GUI2')]),
    (u'Indicate the quantity of requested parts in the Sales quantity field.',
     [(48, 62, 'GUI2')]),
    (u'You can select an input UoM from the input UoM list',
     [(37, 46, 'GUI2')]),
    (u'If the customer has the receive pack size charge/discount check box selected in the customer/order/general tab',
     [(24, 57, 'GUI2'), (84, 106, 'GUI1')]),
    (u'Open the material requisition window and create a new record.',
     [(9, 29, 'GUI1')]),
    (
    u'You have the option to enter an internal destination. Enter either the ID in the internal destination id field or write a description directly in the description field. If you have entered an internal destination ID you can still change the description for this specific material requisition',
    [(81, 104, 'GUI2'), (150, 161, 'GUI2')]),
    (
    u'Project manual connections to the material requisition lines must have been made available on the project /manual connections tab',
    [(98, 125, "GUI1")]),
    (
    u'The project navigator/connections tab and the project/demand/material requisition Line tab will display details of the material requisition line connected to the project activity',
    [(4, 33, "GUI1"), (46, 86, "GUI1")]),
    (u'Open the Material Requisition window, and search for the relevant material requisition.',
     [(9, 29, "GUI1")]),
    (u'The Connect to Activity dialog box opens',
     [(4, 23, "GUI1")]),
    (
    u'You can continue to specify the criteria for the activity you want to select by clicking on the project id, sub project id, and activity id fields',
    [(96, 139, "GUI2")]),
    (u'Alternatively, you can enter the activity sequence in the activity sequence field',
     [(58, 75, "GUI2")]),
    (u'You can obtain the activity sequence from the Project navigator/activity/details tab',
     ([(46, 80, "GUI1")])),
    (
    u'This activity is used to disconnect a manually connected material requisition line from the project activity. You can perform this activity from the material requisition window itself',
    [(149, 169, "GUI1")]),
    (u'The material requisition line will no longer appear as a connection on the project navigator/connections tab.',
     [(75, 104, "GUI1")]),
    (u'Open the material requisition window, and search for the relevant material requisition',
     [(9, 29, "GUI1")]),
    (u'Open the material requisition window and populate or query for the appropriate material requisition.',
     [(9, 29, "GUI1")]),
    (
    u'The parts are reserved in stock and the order line status is updated from Released to Reserved. You can see the quantity of parts reserved in the qty reserved field.',
    [(146, 158, "GUI2")]),
    (u'The Rem Qty to Res field of the manual reservation dialog box shows how many parts remain to be reserved',
     [(4, 19, "GUI2"), (32, 50, "GUI1")]),
    (u'You can also remove a reservation by entering a negative quantity in the reserve qty field.',
     [(73, 84, "GUI2")]),
    (
    u'The parts are reserved and the requisition line status is updated from Released to Reserved. You can see how many parts are reserved in the qty reserved column.',
    [(140, 152, "GUI2")]),
    (u'Select the Reserve Manually function in the Operations menu. The manual reservation dialog box opens up.',
     [(65, 84, "GUI1")]),
    (
    u'In the line for the proper inventory location, enter the quantity that you want to reserve in the reserve qty field.',
    [(98, 110, "GUI2")]),
    (u'You can see the quantity to be reserved in the rem qty to res field.',
     [(47, 61, "GUI2")]),
    (u'Open the Serial Parts window. You can also perform this procedure from the serial part window.',
     [(75, 86, "GUI1")]),
    (u'In the Condition Code, cond limit description, and standard value fields',
     [(7, 45, "GUI2"), (51, 65, "GUI2")]),
    (u'Click the task cards tab and create a new record',
     [(10, 20, "GUI1")]),
    (u'Click the task cards tab and then click the task cards sub tab',
     [(10, 20, "GUI1"), (44, 54, "GUI1")]),
    (u'In the task card id field',
     [(7, 19, "GUI2")]),
    (u'revert to the default value by selecting the reset serial base number check box.',
     [(45, 68, "GUI2")]),
    (u'Click OK.',
     [(6, 8, "ACTION")]),
    (u'If needed, modify the serial base number ',
     [(22, 40, "ACTION")]),
    (u'Right-click and click manage serial number generation',
     [(22, 53, "ACTION")]),
    (u'When serial parts are defined, the life limited field does not display any value',
     [(35, 53, "GUI2")]),
    (u'Use the bp links portlet for maintaining all links to cubes and scorecards you deal with on a regular ',
     [(8, 16, "GUI1")]),
    (u'Open the document info page to get detailed information on the document',
     [(9, 22, "GUI1")]),
    (u'Enter all required data in the copy parts to site dialog box',
     [(32, 49, "GUI1")]),
    (u'On the navigate menu',
     [(7, 15, "GUI2")]),
    (u'You can enter new values for the proposed schedule on the proposed schedule tab ',
     [(58, 75, "GUI1")]),
    (u'the work load for the work centers can be compared on the schedule analysis and load analysis tabs',
     [(58, 75, "GUI1"), (80, 93, "GUI1")]),
    (u'Enter a description in the quotation desc field.',
     [(27, 41, "GUI2")]),
    (u'enter suitable dates in the request receipt date and price effective date fields.',
     [(28, 48, "GUI2"), (53, 73, "GUI2")]),
    (u' Engineering parts can also be inserted in the engineering parts window',
     [(46, 63, "GUI1")]),
    (u'Use the calculate characteristics menu option to calculate the characteristics for a part.',
     [(8, 33, "GUI2")]),
    (u'Right-click and click Add Labor Clocking.',
     [(22,40,"ACTION")]),
    (u'Right-click and click add labor clocking.',
     [(22,40,"ACTION")]),
    (u'Click OK.',
     [(6,8,"ACTION")]),
    (u'Click ok',
     [(6,8,"ACTION")]),
    (u'click ok',
     [(6,8,"ACTION")]),
    (u'Right-click and click Add Machine Clocking',
     [(22,42,"ACTION")]),
    (u'Right-click and click add machine clocking',
     [(22,42,"ACTION")]),
    (u'Right-click and click Add Indirect Labor Clocking',
     [(22,49,"ACTION")]),
    (u'Right-click and click Add Indirect Labor Clocking',
     [(22,49,"ACTION")]),
    (u'Right-click and click Add Machine Downtime Clocking',
     [(22,51,"ACTION")]),
    (u'Right-click and click add machine downtime clocking',
     [(22,51,"ACTION")]),
    (u'By selecting the Show Operation Clockings option, machine, labor and interruption clockings recorded on the selected shop order operation will be shown',
     [(17,41,"GUI2")]),
    (u'By selecting the show operation clockings option, machine, labor and interruption clockings recorded on the selected shop order operation will be shown',
     [(17,41,"GUI2")]),
    (u'while stopped clockings will be shown only if their start time is later than the past number of days defined in the Object Properties/Shop Floor Workbench dialog box',
     [(116,154,"GUI1")]),
    (u'while stopped clockings will be shown only if their start time is later than the past number of days defined in the object properties/shop floor workbench dialog box',
     [(116,154,"GUI1")]),
    (u'For machine and interruption clockings, the Cancel Stop option is only available for the latest clocking for each operation',
     [(44,55,"GUI2")]),
    (u'For machine and interruption clockings, the Cancel Stop option is only available for the latest clocking for each operation',
     [(44,55,"GUI2")]),
    (u'The Cancel Team Stop option is only available for the latest clocking for each operation with a team stamp for each employee.',
     [(4,21,"GUI2")]),
    (u'The cancel team stop option is only available for the latest clocking for each operation with a team stamp for each employee.',
     [(4,21,"GUI2")]),
    (u'To cancel stop time, right-click on the operation line and click Cancel Stop or Cancel Team Stop',
     [(65,76,"GUI2"),(80,96,"GUI2")]),
    (u'To cancel stop time, right-click on the operation line and click Cancel Stop or Cancel Team Stop',
     [(65,76,"GUI2"),(80,96,"GUI2")]),
    (u'Right-click and click Add Indirect Labor Result.',
     [(22,47,"GUI2")]),
    (u'Right-click and click add indirect labor result.',
     [(22,47,"GUI2")]),
    (u'In the Time Card - Day window, search for the employee for which you want to add an indirect report',
     [(7,22,"GUI1")]),
    (u'In the time card - day window, search for the employee for which you want to add an indirect report',
     [(7,22,"GUI1")]),
    (u'In the Operation Reports tab, select the operation report you wish to adjust, right-click and click Adjust Operation Results, the Adjust Operation Result dialog will appear',
     [(7,24,"GUI1"),(100,124,"GUI2"),(137,153,"GUI1")]),
    (u'In the operation reports tab, select the operation report you wish to adjust, right-click and click Adjust operation results, the adjust operation result dialog will appear',
     [(7,24,"GUI1"),(100,124,"GUI2"),(137,153,"GUI1")]),
    (u'If required, also enter a new value in the Resource Share field.',
     [(43,57,"GUI2")]),
    (u'If required, also enter a new value in the resource share field.',
     [(43,57,"GUI2")]),
    (u'To adjust a machine result, enter the new value(s) in the Mach Setup and/or Mach Run fields.',
     [(58,68,"GUI2"),(76,84,"GUI2")]),
    (u'To adjust a machine result, enter the new value(s) in the mach setup and/or mach run fields.',
     [(58,68,"GUI2"),(76,84,"GUI2")]),
    (u'Right-click and click adjust operation results, the adjust operation result dialog will appear.',
     [(22,46,"ACTION"),(52,75,"GUI1")]),
    (u'Right-click and click Adjust Operation Results, the Adjust Operation Result dialog will appear. ',
     [(22,46,"ACTION"),(52,75,"GUI1")]),
    (u'If the Adjust Schedule Due To Shop Floor Reporting check box has been selected in the Scheduling Basic Data/Shop Order Scheduling/Scheduling Server tab, the schedule will be adjusted to reflect the reported time.',
     [(7,50,"GUI2"),(86,147,"GUI1")]),
    (u'If the Adjust schedule due to shop floor reporting check box has been selected in the scheduling basic data/shop order scheduling/scheduling server tab, the schedule will be adjusted to reflect the reported time.',
     [(7,50,"GUI2"),(86,147,"GUI1")]),
    (u'If Buffered Operations Reporting is enabled and the Adjust Schedule Due To Shop Floor Reporting check box in the Scheduling Basic Data/Shop Order Scheduling/Scheduling Server tab has been selected, at the next execution of buffered operations reporting the scheduling server will adjust the operation time due to remaining quantity and',
     [(52,95,"GUI2"),(113,174,"GUI1")]),
    (u'If Buffered Operations Reporting is enabled and the adjust schedule due to shop floor reporting check box in the scheduling basic data/shop order scheduling/scheduling server tab has been selected, at the next execution of buffered operations reporting the scheduling server will adjust the operation time due to remaining quantity and',
     [(52,95,"GUI2"),(113,174,"GUI1")])

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
nlp.entity.add_label(entity_label3)


ner = train_ner(nlp, train_data, output_directory)

