import en_gui1
import sys
import simplejson as json

#read json object
#myjson = json.loads(sys.stdin.read())
#para=myjson["param"]

nlp = en_gui1.load()
para='The customer should have a record in the customer window'
unicodePara=unicode(para)

doc = nlp(unicodePara)            # See "Using the pipeline"
guiElements=[(w.text) for w in doc if w.ent_type_=="GUI1"]

#print(str(guiElements[0]))
print("success")
