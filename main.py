from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/sign-up')
def display_sign_up_form():
    return render_template('sign_up_form.html')

def field_is_blank(field):
    if field == '':
        return False
    else:
        return True

@app.route('/sign-up', methods=['POST'])
def sign_up():

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    blank_field = ''
    username_invalid = ''
    password_invalid = ''
    bad_match = ''
    email_invalid = ''

    if field_is_blank(username):
        blank_field = "This field was left blank."
    else:
        username = username
    if field_is_blank(password):
        blank_field = "This field was left blank."
    else:
        password = password
    if field_is_blank(verify):
        blank_field = "This field was left blank."
    else:
        verify = verify

    if not blank_field:
        return redirect('/valid-form')
    else:
        return render_template('sign_up_form.html', blank_field=blank_field,
            username_invalid=username_invalid, password_invalid=password_invalid,
            bad_match=bad_match, email_invalid=email_invalid,
            username=username, password=password, verify=verify,
            email=email)

@app.route('/valid-form')
def valid_form():
    return '<h1>Thanks for signing up!</h1>'


if __name__ == "__main__":
    app.run()
