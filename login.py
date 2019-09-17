# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 12:02:09 2019

@author: AnkitaDatta
"""

from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success',name = user))
    
if __name__  == '__main__':
    app.run(host = '127.0.0.1' , port= 5003)
