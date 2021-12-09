from . import pages
from flask import render_template

@pages.route('/')
def home():
    return render_template('pages/home.html')

@pages.route('/about')
def about():
    return render_template('pages/about.html')