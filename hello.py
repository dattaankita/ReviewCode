# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 15:03:09 2019

@author: AnkitaDatta
"""


from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/<user>')
def hello_name(user):
    return render_template('hello.html', name = user)


if __name__ == '__main__':
    #app.run(debug= True)
    app.run(host= '127.0.0.2', port = 5006, debug=True)