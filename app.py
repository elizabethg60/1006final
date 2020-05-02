# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: etill
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def home():
    return("Hello! My name is Elizabeth Gonzalez. I am a first year at CU and my intended major is astrophysics.")

#start the server
if __name__ == "__main__":
    app.run()