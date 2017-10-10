from flask import Flask, request, redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG']= True

@app.route('/index')
def display_index():
    template = jinja_env.get_template('./index.html')
    return template.render()

@app.route('/signup')
def display_signup_form():
    template = jinja_env.get_template('./signup_form.html')
    return template.render()

# THESE DEF FUNCTIONS NEED TO BE BOOLEAN EXPRESIONS
# LIKE THESE
# try:
#     int(num)
#     return True
# except ValueError:
#     return False

def valid_user_name():
    return

def valid_password():
    return

def valid_password_check():
    return

def valid_email(email):
    
    
    #char = 'email'
    return "char + '@' + char + '.' + len(char.isalpha == 3)"

@app.route('/signup', methods=['POST'])
def process_sign_up_form():

    user_name = request.form['user_name']
    password = request.form['new_password']
    password_check = request.form['password_check']
    email = request.form['email']

    user_name_error = ''
    password_error = ''
    password_check_error = ''
    email_error = ''
    return


app.run()