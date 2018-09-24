#import statements go here 
from flask import Flask, request, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import Required, Email

import requests
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.debug = True

@app.route('/')
def home():
	return "Hello, world!"
	
#create class to represent WTForm that inherits flask form
class itunesform(FlaskForm):
	artist = StringField('Enter an artist name. ', validators=[Required()])
	api = IntegerField('Enter the number of results. ', validators=[Required()])
	email = StringField('What is your email? ', validators=[Required(), Email() ])
	submit = SubmitField('Submit')

@app.route('/itunes-form')
def itunes_form(FlaskForm):
	simpleForm = itunesform()
	return render_template('itunes-form.html', form=simpleForm) # HINT : create itunes-form.html to represent the form defined in your class

@app.route('/itunes-result', methods = ['GET', 'POST'])
def itunes_result():
	form = itunesform(request.form)
	if request.method == 'POST' and form.validate_on_submit():
		artist = form.artist.data
		email = form.email.data
		api = form.api.data

		baseurl = 'https://itunes.apple.com/search'
		params_diction = {}
		params_diction['term'] = artist
		params_diction['country'] = "US"
		params_diction['limit'] = api
		response = requests.get(baseurl, params = params_diction)
		response_py = json.loads(response.text)['results']
	# HINT : create itunes-results.html to represent the results and return it
	flash('All fields are required!')
	return redirect(url_for('itunes-results')) #this redirects you to itunes_form if there are errors


if __name__ == '__main__':
	app.run()
