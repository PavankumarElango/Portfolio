# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 15:57:56 2020

@author: pavan
"""

from flask import Flask, render_template

server = Flask(__name__)
server.debug = True
@server.route('/')
def landing_page():
    return render_template('index.html')
    
if __name__ == '__main__':
    server.run(debug=True)