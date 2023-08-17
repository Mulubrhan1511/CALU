from flask import Flask, render_template, request, redirect, flash, url_for
from models import app, db, User
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os


with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/clubs')
def clubs():
    return render_template('clubs.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    
    if request.method == 'POST':
        #Get the form data
        full_name = request.form['username']
        email = request.form['email']
        password = request.form['password']
        gender = None
        study = None
        major = None


        #Check if the email is already registered
        user = User.query.filter_by(email=email).first()
        if user:
             flash('Email address already exists', 'error')
             return redirect(url_for('new_worker'))

        #  Hash the password
        hashed_password = generate_password_hash(password, method='sha256')
        image_path = None
        new_user = User(
            full_name=full_name,
            email=email,
            password=hashed_password,
            gender=gender,
            study=study,
            major=major,
            image=image_path
        )
        db.session.add(new_user)
        db.session.commit()
         #Add the new user to the database
        return redirect(url_for('signup'))

    #Render the signup page
    return render_template('signup.html')
if __name__ == '__main__': 
   app.run()