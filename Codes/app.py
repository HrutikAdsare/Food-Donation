from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = '35cc94b2b79f4b1664e33c0d3e33cd04'  # Replace with your own secret key for session management

# Configure the SQLite database (you can change this to any database you prefer)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define User model
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# Define Volunteer model
class Volunteer(db.Model):
    __tablename__ = 'volunteers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    location = db.Column(db.String(120), nullable=False)
    availability = db.Column(db.String(120), nullable=False)

# Define Donation model
class Donation(db.Model):
    __tablename__ = 'donations'
    id = db.Column(db.Integer, primary_key=True)
    food_name = db.Column(db.String(120), nullable=False)
    location = db.Column(db.String(120), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Route for the homepage (index.html)
@app.route('/')
def home():
    return render_template('index.html')

# Route for the about page (about.html)
@app.route('/about')
def about():
    return render_template('about.html')

# Route for the signup/login page (auth.html)
@app.route('/auth')
def auth():
    return render_template('auth.html')

# Route for the donate page (donate.html)
@app.route('/donate')
def donate():
    return render_template('donate.html')

# Route for the get involved page (getinvolved.html)
@app.route('/getinvolved')
def getinvolved():
    return render_template('getinvolved.html')

# Route to handle signup (POST method)
@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    
    # Check if the email already exists in the database
    existing_user = User.query.filter_by(email=email).first()
    
    if existing_user:
        flash('Email is already registered. Please log in or use another email.', 'error')
        return redirect(url_for('auth'))
    
    # If email is not in use, proceed to create the new user
    new_user = User(username=username, email=email, password=password)
    
    # Add user to the database
    db.session.add(new_user)
    db.session.commit()

    flash('Signup successful! You can now log in.', 'success')
    return redirect(url_for('auth'))


# Route to handle login (POST method)
@app.route('/login', methods=['POST'])
def login():
    # You can implement login logic here (e.g., check username/password)
    return redirect(url_for('home'))  # Redirect as needed

# Route to handle volunteer registration (POST method)
@app.route('/volunteer_registration', methods=['POST'])
def volunteer_registration():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    location = request.form['location']
    availability = request.form['availability']
    
    new_volunteer = Volunteer(name=name, email=email, phone=phone, location=location, availability=availability)
    
    # Add volunteer to the database
    db.session.add(new_volunteer)
    db.session.commit()

    flash('Registration successful! Thank you for volunteering.', 'success')
    return redirect(url_for('getinvolved'))

# Route to handle food donations (POST method)
@app.route('/donate', methods=['POST'])
def handle_donation():
    food_name = request.form['foodName']
    location = request.form['location']
    quantity = request.form['quantity']
    
    new_donation = Donation(food_name=food_name, location=location, quantity=quantity)
    
    # Add donation to the database
    db.session.add(new_donation)
    db.session.commit()

    flash('Thank you for your donation!', 'success')
    return redirect(url_for('donate'))

@app.route('/users')
def display_users():
    users = User.query.all()  # Fetch all users from the User table
    return render_template('users.html', users=users)



if __name__ == '__main__':
    app.run(debug=True)
