import en_en_gui
import sys
#import simplejson as json
import json


nlp = en_en_gui.load()
para="""Select for the operation for which you want to adjust a report
In the Reports tab, select the Show Operation Reports option.
Select the operation report you wish to adjust, right-click and click Adjust Operation Results, the Adjust Operation Result dialog will appear. 
To adjust a quantity complete result, enter the new value in the Qty Completed field.
To adjust a quantity scrapped result, enter the new value in the Qty Scrapped field. If the part is catch unit handled, also enter a new value in the Catch Qty Scrapped field.
To adjust a machine result, enter the new value(s) in the Mach Setup and/or Mach Run fields. If required, also enter a new value in the Resource Share field.
To adjust a labor result, enter the new value(s) in the Labor Setup and/or Labor Run fields. If required and if the labor is not reported against a specific employee, enter a new value in Crew Size field.
Click OK.
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
#print(formattedGui)

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





