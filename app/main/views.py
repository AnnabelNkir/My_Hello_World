from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from ..models import User
from flask_login import login_required,current_user
from .. import db


#views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data.
    '''
    return render_template('index.html')