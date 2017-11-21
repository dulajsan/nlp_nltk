import en_gui
import sys
#import simplejson as json
import json


nlp = en_gui.load()
para="""Select : for the operation for which you want to adjust a report
In the Reports tab, select the Show Operation Reports option.
Select the operation report you wish to adjust, right-click and click Adjust Operation Results, the Adjust Operation Result dialog will appear. 
To adjust a quantity complete result, enter the new value in the Qty Completed field.
To adjust a quantity scrapped result, enter the new value in the Qty Scrapped field. If the part is catch unit handled, also enter a new value in the Catch Qty Scrapped field.
To adjust a machine result, enter the new value(s) in the Mach Setup and/or Mach Run fields. If required, also enter a new value in the Resource Share field.
To adjust a labor result, enter the new value(s) in the Labor Setup and/or Labor Run fields. If required and if the labor is not reported against a specific employee, enter a new value in Crew Size field.
Click OK.

"""

unicodePara=unicode(para)
jsonlist=[]
doc = nlp(unicodePara)

for ent in doc.ents:
    guijson = {"guiword": str(ent.text), "type": str(ent.label_),"start":ent.start_char,"end":ent.end_char}
    jsonlist.append(guijson)

print(jsonlist)
