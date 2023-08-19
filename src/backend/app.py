from flask import Flask, render_template, request, redirect, flash, url_for
from models import app, db, User
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os
from flask_login import login_user, login_required, logout_user, current_user, LoginManager
app = app

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    # Load the user from the database based on the user ID
    user = None
    if not user:
        user = User.query.get(int(user_id))
    return user

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
        # Get the form data
        full_name = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email address already exists', 'error')
            return redirect(url_for('login'))
        # Hash the password
        hashed_password = generate_password_hash(password, method='sha256')

        new_user = User(
            full_name=full_name,
            email=email,
            password=hashed_password
        )
        db.session.add(new_user)
        db.session.commit()

        flash('Your account has been created successfully. Please log in.', 'success')
        return redirect(url_for('signup'))

    return render_template('signup.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Check if the user is a patient
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            # Log in the patient
            login_user(user, remember=True)
            return render_template('homel.html',user=current_user)
        return "no"

    return render_template('signup.html')

@app.route('/homel')
@login_required
def homel():
    return render_template('homel.html', user=current_user)
@app.route('/clubsl')
@login_required
def clubsl():
    return render_template('clubs-1.html')

@app.route('/aboutl')
@login_required
def aboutl():
    return render_template('about-1.html')
@app.route('/profile')
def profile():
    return render_template('profile.html',user=current_user)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()