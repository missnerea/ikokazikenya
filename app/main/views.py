from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from .. import db,photos
from ..models import Admin,Blogpost,Blogpics
from flask_login import login_required





#Views
@main.route('/')
def index():
    '''
    view  root page function that returns 
    the index page and its data
    '''

    title = 'blog!'
     

    
    return render_template('index.html',title = title,allposts=allposts)


