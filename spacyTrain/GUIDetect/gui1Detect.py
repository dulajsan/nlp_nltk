import en_gui
import sys
#import simplejson as json
import json


nlp = en_gui.load()
para="""
Open the Reporting Period Status window and create a new record.
Enter a value in the Reporting Transaction Type field. The List of Values can be used to select the required value.
Enter a value in the Balance Version field. The List of Values can be used to select the required value.
Enter the starting reporting period in the From Year-Period field. The List of Values can be used to select the required value.
Enter the until reporting period in the Until Year-Period field. The List of Values can be used to select the required value.
Enter a note in the Note field if required.
Save the information.
"""

unicodePara=unicode(para)

doc = nlp(unicodePara)            # See "Using the pipeline"
#guiElements=[(w.text,w.ent_iob,w.ent_type_) for w in doc if w.ent_type_=="GUI1" or w.ent_type_=="GUI2"]
guiElements=[w for w in doc if w.ent_type_=="GUI1" or w.ent_type_=="GUI2" or w.ent_type_=="ACTION"]
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
print(formattedGui)

jsonlist=[]
for q in formattedGui:
        strword=" ".join(str(x) for x in q)
        if "/" in strword:
            strword="".join(strword.split())
        print(strword)
        guijson={"guiword":strword,"type":str(q[0].ent_type_)}
        jsonlist.append(guijson)


print (jsonlist)







#formattedGui=[]





