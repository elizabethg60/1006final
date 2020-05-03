# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: Elizabeth Gonzalez 
eg3055
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def home():
    return render_template('index.html')

#classes link
@app.route("/classes")
def classes():
    return render_template('classes.html')

#assignments link
@app.route("/assignments")
def assignments():
    return render_template('assignments.html')
    
    
#start the server
if __name__ == "__main__":
    app.run()