from flask import Flask
from flask import request
import json
import os
from utils import ner
from flask import jsonify


dirname, filename = os.path.split(os.path.abspath(__file__))
print("running from", dirname)
print("file is", filename)


app = Flask(__name__)



@app.route('/hello')
def hello_world():
    return 'Hello, World!'


from flask import render_template

@app.route('/')
def main(name=None):
    return render_template('index.html', name=name)

@app.route('/submitText', methods = ['POST', 'GET'])
def nlp():
    text = request.form.get('message')
    ents = ner.NLP.ner(text)
    print(ents)
    return jsonify(ents)

@app.route('/csv', methods = ['POST', 'GET'])
def upload():
    if request.method == 'GET':
        return render_template('csv_upload.html', name='sasa')
    else:
        f = request.files['csv_file']
        f.save(dirname + "/entities_files/" + f.filename)
        return 'Your file is successfully uploaded'
