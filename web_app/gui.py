from flask import Flask,json,request,jsonify,current_app,Response,make_response
from flask_cors import CORS
from functools import wraps
from flask_jsonpify import jsonify
from json import dumps


#nlp
import en_gui #gui type 1 detection

nlp = en_gui.load()


app = Flask(__name__)
CORS(app)

def support_jsonp(f):

    """Require user authorization"""

    @wraps(f)
    def decorated_function(*args, **kwargs):
        callback = request.args.get('callback', False)
        if callback:
            content = str(callback) + '(' + json.dumps(dict(*args, **kwargs)) + ')'
            return current_app.response_class(content, mimetype='application/json')
        else:
            return f(*args, **kwargs)
    return decorated_function


@app.route("/writetocsv",methods=['GET'])
def writetofile():
    word=request.args.get('word')
    meaning=request.args.get('meaning')

    with open("C:/Users/dusalk/Documents/visual studio 2015/Projects/WordWebAddIn1/WordWebAddIn1Web/Resources/csv/abbreviations.csv","a") as fo:
        fo.write("\n"+str(word)+","+str(meaning))
    return '{success:true}'
   

 
@app.route("/",methods=['GET'])
def hello():
    paragraph=request.args.get('paragra')
    #paragraph='If the Input UoM Group check box on the line is selected'

    #nlp
    unicodePara=unicode(paragraph)
    doc = nlp(unicodePara)
    jsonlist=[]
    for ent in doc.ents:
        guijson = {"guiword": str(ent.text), "type": str(ent.label_),"start":ent.start_char,"end":ent.end_char}
        jsonlist.append(guijson)

            
    jsonstr=json.dumps(jsonlist)
   
    #return json.dumps(formattedGui)
    #return make_response(dumps(guiElements))
    return jsonify(Gui=jsonlist)
    
    #return jsonify({"status": str(guiElements[0])})

if __name__ == "__main__":
    app.run()
