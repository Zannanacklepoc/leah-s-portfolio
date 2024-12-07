from flask_app import app
from flask import render_template, redirect, request, session, flash

@app.route('/')
def default():
	return render_template ('portfolio.html')

@app.route('/blog')
def blog():
	return render_template ('blog.html')

@app.route('/projects')
def projects():
	return render_template ('projects.html')