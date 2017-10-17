import en_gui
import sys
#import simplejson as json
import json


nlp = en_gui.load()
para=""" The customer should have a record in the customer window'
The user should be connected to a coordinator in the sites to site entity window 
Open the desired sales quotation and select the Quotation Lines tab.
If the Input UoM Group check box on the line is selected' 
Open the desired sales quotation and select the Quotation Lines tab. """
unicodePara=unicode(para)

doc = nlp(unicodePara)            # See "Using the pipeline"
#guiElements=[(w.text,w.ent_iob,w.ent_type_) for w in doc if w.ent_type_=="GUI1" or w.ent_type_=="GUI2"]
guiElements=[w for w in doc if w.ent_type_=="GUI1" or w.ent_type_=="GUI2"]
#print(guiElements)

i=0
temp=[]
formattedGui=[]
temp=guiElements
s=1;
for t in guiElements:
    #print(t.ent_iob)
    if t.ent_iob==3 and i!=0:
        formattedGui.append(temp[:s])
        temp=guiElements[i:]
        s=1;
    elif i==len(guiElements)-1:
        formattedGui.append(temp)
        s=1;
    elif t.ent_iob==1:
        s+=1;

    i+=1
#print(formattedGui)

jsonlist=[]
for q in formattedGui:
        strword=" ".join(str(x) for x in q)
        #print(strword)
        guijson={"guiword":strword,"type":str(q[0].ent_type_)}
        jsonlist.append(guijson)


print (jsonlist)






#formattedGui=[]





