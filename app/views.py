"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
import datetime
from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash, session, abort
from app.models import UserProfile
from .forms import ProfileForm
from datetime import date, time
from werkzeug.utils import secure_filename

@app.route('/')
def home():
    return render_template('home.html')
    
@app.route('/about/')
def about():
    return render_template('about.html')

#####################################################################

@app.route('/profile', methods = ['POST', 'GET'])
def profile():
    form = ProfileForm()
    if request.method == "POST" and form.validate_on_submit():
        
        #userid  = str
        first_name  = request.form.data['first_name']
        last_name   = request.form.data['last_name']
        gender      = request.form.data['gender']
        email       = request.form.data['email']
        location    = request.form.data['location']
        biography   = request.form.data['biography']
        created_on  = time.strftime('%Y/%b/%d')
        
        photo = request.files.data['file']
        if photo:
            filename = secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOAD FOLDER'], filename))
            
        user = UserProfile(first_name='first_name', last_name='last_name', gender='gender',
        email='email', location='location', biography='biography', photo='photo', created_on='created_on')
        db.session.add(user)
        db.session.commit()
    return render_template('profile.html', form = form)
    
    


@app.route('/profiles', methods = ['POST', 'GET'])
def profiles():
    return render_template('profiles.html', profile = profiles)
    


@app.route('/profile/<userid>', methods = ['POST', 'GET'])

#####################################################################

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
