# Import necessary modules from Flask
from flask import Flask, render_template, request, redirect, url_for, session

# Create a Flask application instance
app = Flask(__name__)

# Set a secret key for session management
app.secret_key = 'your_secret_key'

# Mock user database (replace it with a real one)
users = {'user1': 'password1', 'user2': 'password2'}

# Define route for the home page
@app.route('/')
def index():
    # Check if user is logged in
    if 'username' in session:
        # Render the home page template with the username
        return render_template('index.html', username=session['username'])
    # If not logged in, redirect to the login page
    return redirect(url_for('login'))

# Define route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    # If the form is submitted
    if request.method == 'POST':
        # Get username and password from the form
        username = request.form['username']
        password = request.form['password']
        # Check if username and password match the mock user database
        if username in users and users[username] == password:
            # Set session variable for the logged-in user
            session['username'] = username
            # Redirect to the home page
            return redirect(url_for('index'))
        else:
            # If credentials are incorrect, render login page with error message
            return render_template('login.html', error='Invalid username or password.')
    # If it's a GET request, render the login page
    return render_template('login.html')

# Define route for logging out
@app.route('/logout')
def logout():
    # Clear session variable for the logged-in user
    session.pop('username', None)
    # Redirect to the home page
    return redirect(url_for('index'))

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
