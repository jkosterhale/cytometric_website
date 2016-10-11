import flask
from flask import render_template, request, jsonify
from app import app
import numpy as np
import pickle
import json

import sys
sys.path.append('/Users/jorie/Dropbox (Personal)/Insight_Personal/empath-master')
#sys.path.append('/Users/jorie/Dropbox (Personal)/Insight_Personal/empath-master/data/')
#sys.path.append('/Users/jorie/Dropbox (Personal)/Insight_Personal/empath-master/drug_data/')
#sys.path.append('/Users/jorie/Dropbox (Personal)/Insight_Personal/empath-master/NLP/')
#sys.path.append('/Users/jorie/Dropbox (Personal)/Insight_Personal/empath-master/scraper/')
#sys.path.append('/Users/jorie/Dropbox (Personal)/Insight_Personal/empath-master/app/app/')


@app.route('/index')
@app.route('/')
def input():
	return render_template('input.html')

@app.route('/output')
def output():
	# pull drug name from request field, check for match
	classtype = request.args.get('classtype')
	datasource = request.args.get('datasource')
	

	# feed the data into the algorythm and produce a figure
	#dataout, ploturl1, ploturl2, info, sourcename = clusterme(datasource)
	#ploturl = ploturl2,
		#dataout=dataout,
		#sourcename=sourcename,
		#info = info)
	sourcename = "Data"
	info = .89

	return render_template('output.html')
		

@app.route('/contact')
def contact():
	"""renderer for contact page.
	"""
	return render_template('contact.html')


@app.route('/about')
def about():
	"""renderer for about page.
	"""
	return render_template('about.html')




