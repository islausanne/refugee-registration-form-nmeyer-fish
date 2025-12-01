from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for flash messages

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Registration form page
@app.route('/register')
def register():
    return render_template('register.html')

# Handle form submission (students will add JSON save code here)
@app.route('/submit', methods=['POST'])
def submit_form():
    first_name = request.form['first_name']
    sur_name = request.form['sur_name']
    country = request.form['country']
    age = request.form['age']
    email = request.form['email']
    gender = request.form['gender']
    date_of_birth = request.form['date_of_birth']
    phone = request.form['phone']


    # Check if file exists
    if os.path.exists('registrations.json'):
        with open('registrations.json', 'r') as file:
            data = json.load(file)
    else:
        data = []

    # Add the new registration
    data.append({'first_name': first_name, 'sur_name':sur_name, 'country': country, 'age': age, 'email': email, 'gender': gender, 'date_of_birth': date_of_birth, \
                 'phone':phone})

    # Save all registrations back to the file
    with open('registrations.json', 'w') as file:
        json.dump(data, file, indent=2)

    return redirect(url_for('index'))

# Display stored registrations (students will add JSON reading code here)
@app.route('/view')
def view_registrations():
    with open('registrations.json', 'r') as file:
        data = json.load(file)
    return render_template('view.html', registrations=data)

if __name__ == '__main__':
    app.run(debug=True)



