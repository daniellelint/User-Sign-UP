from flask import Flask, request, redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    template = jinja_env.get_template('index_page.html')
    return template.render()

@app.route("/log-in")
def log_in():
    template = jinja_env.get_template('home_template.html')
    return template.render()

@app.route('/sign_up')
def display_sign_up():
    template = jinja_env.get_template('sign_up_form.html')
    return template.render()

@app.route('/sign_up', methods=['POST'])
def validate_sign_up():
    template = jinja_env.get_template('sign_up_form.html')

    user_name_error = ''
    user_name = request.form['user_name']
    if len(user_name) > 20 or len(user_name) < 3:
        user_name_error = "User Name length requirements: 3 - 20 Characters Only"
    if " " in user_name:
        user_name_error = "User Name must not contain spaces."
    if len(user_name) == 0:
        user_name_error = "User Name required to submit."
    
    password_error = ''
    password = request.form['password']
    if len(password) > 20 or len(password) < 3:
        password_error = "Password length requirements: 3 - 20 Characters Only"
    if " " in password:
        password_error = "Password must not contain spaces."
    if len(password) == 0:
        password_error = "Password required to submit."
    
    password_check_error = ''
    password_check = request.form['password_check']    
    if password != password_check:
        password_check_error = "Passwords must match."
    if len(password_check) > 20 or len(password_check) < 3:
        password_check_error = "Password length requirements: 3 - 20 Characters Only"
    if " " in password_check:
        password_check_error = "Password must not contain spaces."
    if len(password_check) == 0:
        password_check_error = "Password required to submit."

    email_error = ''
    email = request.form['email']
    valid_char = ['@', '.']
    if not email == "":
        for single_char in valid_char:
            if single_char not in email:
                email_error = "Input requires the following characters to be a valid email address: @, ."
        if " " in email:
            email_error = "Email address cannot contain spaces."
        if len(email) > 20 or len(email) < 3:
            email_error = "Email length requirements: 3 - 20 Characters Only"

    if not user_name_error and not password_error and not password_check_error and not email_error:
        return redirect('/signup-success?user_name={0}'.format(user_name))
    else:
        return template.render(user_name_error = user_name_error, 
                                user_name = user_name, password_error = password_error, 
                                password_check_error = password_check_error, 
                                email_error = email_error, email = email)

@app.route('/signup-success')
def valid_signup():
    user_name = request.args.get('user_name')
    template = jinja_env.get_template('welcome_template.html')
    return template.render(user_name=user_name)

app.run()