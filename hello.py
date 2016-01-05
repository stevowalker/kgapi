# import all libraries

import json
import urllib
from flask import Flask, request, render_template, url_for, redirect, jsonify, send_file



# start flask application

app = Flask(__name__)

# map the query form entry to the homepage url '/'

@app.route('/')

# create function that requests the '/results' page and stores form submit
# to the variable query. Once complete, redirect user to the '/results page'.

def entity_query():
	return render_template('/query_form.html')

@app.route('/results', methods=['POST'])
def results():
	query = request.form['entity']
	service_url = 'https://kgsearch.googleapis.com/v1/entities:search'
	params = {
	    'query': query,
	    'limit': 20,
	    'indent': True,
	    'key': 'AIzaSyCm7U8piSUs8op-e850Dc7mx6ZnlKqxnRs',
	    'languages': 'en',
	}
	url = service_url + '?' + urllib.urlencode(params)
	
	response = json.loads(urllib.urlopen(url).read())

	try:
		topten_namedesc = response['itemListElement']
	except KeyError:
		return render_template('/no-query.html')

	return render_template('/results.html', query=query, topten_namedesc=topten_namedesc)

	

@app.route('/about')
def about():
	return render_template('/about.html')

@app.route('/contact')
def contact():
	return render_template('/contact.html')

if __name__ == '__main__':
    app.debug = True
    app.run()