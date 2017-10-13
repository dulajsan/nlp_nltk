import en_gui
import sys
#import simplejson as json
import json


nlp = en_gui.load()
#para='The customer should have a record in the customer window'
#para='The user should be connected to a coordinator in the sites to site entity window'
#para='Open the desired sales quotation and select the Quotation Lines tab.'
#para= 'If the Input UoM Group check box on the line is selected'
para='Open the desired sales quotation and select the Quotation Lines tab'
unicodePara=unicode(para)

doc = nlp(unicodePara)            # See "Using the pipeline"
#guiElements=[(w.text,w.ent_iob,w.ent_type_) for w in doc if w.ent_type_=="GUI1" or w.ent_type_=="GUI2"]
guiElements=[w for w in doc if w.ent_type_=="GUI1" or w.ent_type_=="GUI2"]

i=0
temp=[]
formattedGui=[]
temp=guiElements
for t in guiElements:
    if t.ent_iob==3 and i!=0:
        formattedGui.append(temp[:i])
        temp=guiElements[i:]
    elif i==len(guiElements)-1:
        formattedGui.append(temp)

    i+=1

for q in formattedGui:
    print (q)








#formattedGui=[]





