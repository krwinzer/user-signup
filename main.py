from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/sign-up')
def display_sign_up_form():
    return render_template('sign_up_form.html')

@app.route('/sign-up', methods=['POST'])
def sign_up():

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

# ------------Blank Fields ---------------

    un_blank_field = ''
    pw_blank_field = ''
    verify_blank_field = ''

    if len(username) == 0:
        un_blank_field = "This field was left blank."
    else:
        username = username
    if len(password) == 0:
        pw_blank_field = "This field was left blank."
    else:
        password = password
    if len(verify) == 0:
        verify_blank_field = "This field was left blank."
    else:
        verify = verify

# --------Invalid Username, Password, Email-------------
    username_invalid = ''
    password_invalid = ''
    email_invalid = ''

    if len(username) != 0:
        if len(username) < 4 or len(username) > 19 or ' ' in username:
            username_invalid = "The username must be between 4 and 19 characters long and cannot contain spaces."
        else:
            username = username

    if len(password) != 0:
        if len(password) < 4 or len(password) > 19 or ' ' in password:
            password_invalid = "The password must be between 4 and 19 characters long and cannot contain spaces."
        else:
            password = password

    if len(email) > 0:
        if len(email) < 4 or len(email) > 40 or ' ' in email or '@' not in email or '.' not in email:
            # if '@' not in email and '.' not in email:
            email_invalid = 'Email must be between 4 and 20 characters long, cannot contain spaces, and must be in proper email format.'
        else:
            email = email

# --------Password and Verify Do Not Match----------

    bad_match = ''

    for char, letter in zip(password, verify):
        if char != letter:
            bad_match = 'Passwords do not match.'
            password = ''
            verify = ''
        else:
            verify = verify
            password = password

    if not un_blank_field and not pw_blank_field and not verify_blank_field and not username_invalid and not password_invalid and not email_invalid and not bad_match:
        return render_template('welcome.html', username=username)
    else:
        return render_template('sign_up_form.html', un_blank_field=un_blank_field,
            pw_blank_field=pw_blank_field, verify_blank_field=verify_blank_field,
            username_invalid=username_invalid, password_invalid=password_invalid,
            bad_match=bad_match, email_invalid=email_invalid,
            username=username, password=password, verify=verify,
            email=email)


if __name__ == "__main__":
    app.run()
