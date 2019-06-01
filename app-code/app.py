#! /usr/bin/env python

from flask import Flask, render_template 
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('landing.htm')

@app.route('/about')   
def about():
    dict = {'DataScience':'+1 yrs','Jupyter Notebook':'+1 yrs','Python':'+2 yrs','PostgreSQL':'+3 yrs'}   
    return render_template('about.htm', result = dict)
  
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)
