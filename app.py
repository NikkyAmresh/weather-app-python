from flask import Flask, jsonify, render_template, request 
import sqlite3
from search import id,name,ct
import api
app = Flask(__name__)
@app.route('/',methods = ['POST', 'GET'])
def index():
    d=api.get_forcast(float(72.8777),float(19.0760), 0)
    db=api.get_forcast(float(72.8777),float(19.0760), 1)
    return render_template('index.html',d=d,db=db,len=len(db['list']))
@app.route('/city/<num>',methods = ['POST', 'GET'])
def city(num):
    d=api.get_city(num, 0)
    db=api.get_city(num, 1)
    return render_template('city.html',d=d,db=db, len=len(db['list']))
@app.route('/cityc/<num>',methods = ['POST', 'GET'])
def cityc(num):
    d=api.get_city(num, 0)
    return jsonify(d)
@app.route('/cityf/<num>',methods = ['POST', 'GET'])
def cityf(num):
    db=api.get_city(num, 1)
    return jsonify(db)

@app.route('/api/<lat>/<lon>/', methods=['POST', 'GET'])
def getfc(lat,lon):
    d=api.get_forcast(float(lat),float(lon), 0)
    return jsonify(d)
@app.route('/forecast/<lat>/<lon>/', methods=['POST', 'GET'])
def getfcr(lat,lon):
    d2=api.get_forcast(float(lat),float(lon), 1)
    return jsonify(d2) 
@app.route('/search/<q>',methods = ['POST', 'GET'])
def search(q):
    arr=[]
    for i in range(0,len(name)):
        if name[i].upper().find(q.upper())!=-1:
            if len(arr)<10: 
                arr.append({'id':id[i],'name':name[i],'ct':ct[i]})
            else:
                break;
    return jsonify(arr)
if __name__ == '__main__':
    app.run(debug = True)
  
