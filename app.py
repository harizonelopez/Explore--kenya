from flask import Flask, render_template, request, flash, redirect, url_for, get_flashed_messages
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, logout_user, LoginManager, current_user, login_required
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new_database.db'
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'aladinh00-010montext')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    destination = db.Column(db.String(100), nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

with app.app_context():
    db.create_all()

login_manager.login_view = 'signup' # Redirects to the signup page if the user is not logged in
login_manager.login_message_category = 'danger' # Shows the danger message if the user is not logged in

def get_flash_messages():
    messages = get_flashed_messages()
    return [(message, 'info') for message in messages]  

@app.route('/')
def home():
    flash_messages = get_flash_messages()
    return render_template("index.html", flash_messages=flash_messages)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email address already registered. Login instead', 'danger')
            return redirect(url_for('login'))
        
        new_user = User(username=username, email=email, password=generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()

        flash('User account created successfully! Login now', 'success')
        return redirect(url_for('login'))
    
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():    
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Email or password mismatch', 'danger')

    return render_template('login.html')

@app.route('/booking', methods=['GET', 'POST'])
@login_required # Redirects to the login page if the user is not logged in
def booking():
    if request.method == 'POST':
        destination = request.form['destination']
        cost = int(request.form['cost'])
        
        new_booking = Booking(destination=destination, cost=cost, user_id=current_user.id)
        db.session.add(new_booking)
        db.session.commit()

        flash(f'Hey {current_user.username}, you have successfully booked {destination} as your destination tour place.', 'success')
        return redirect(url_for('booking'))
    return render_template('book.html')

@app.route('/_policy')
def policy():
    return render_template('policy.html')

@app.route('/_guide')
def guide():
    return render_template('guide.html')

@app.route('/faq_questions')
def faq():
    return render_template('faq.html')

@app.route('/_contacts')
def contact():
    return render_template('contact.html')

@app.route('/_terms')
def terms():
    return render_template('terms.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)