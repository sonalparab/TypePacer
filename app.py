from flask import Flask, render_template, request, session, redirect, url_for, flash
import os, sqlite3, hashlib
import db_builder

#THIS FIXES ENCODE ERROR
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#===
app= Flask(__name__)
app.secret_key = os.urandom(64)
db_builder.createTables()


SUCCESS = 1
BAD_PASS = -1
BAD_USER = -2

# Methods

#encrypts password
def encrypt_password(password):
    encrypted_pass = hashlib.sha1(password.encode('utf-8')).hexdigest()
    return encrypted_pass

#authenticate username and password
def authenticate(username, password):
    users = db_builder.user_dict()
    if username in users.keys():
        if password == users[username]:
            return SUCCESS
        else:
            return BAD_PASS
    else:
        return BAD_USER

#check if username already exists
def check_newuser(username):
    users = db_builder.user_dict()
    if username in users.keys():
        return BAD_USER
    return SUCCESS



@app.route('/', methods=['POST', 'GET'])
#login page if user is not in session, otherwise welcome
def root():
    if 'user' not in session:
        return render_template('login.html', title="Login")
    else:
        return redirect( url_for('welcome') )

@app.route('/welcome', methods=['POST', 'GET'])
#welcomes user or redirects back to root if logged out
def welcome():
    if 'user' not in session:
        return redirect( url_for('root') )
    else:
        return render_template('welcome.html', user=session['user'], title='Welcome')

@app.route('/logout', methods=['POST', "get"])
#removes user from session
def logout():
    if 'user' in session:
        flash(session['user'] + " logged out.")
        session.pop('user')
    return redirect( url_for('root') )


@app.route('/auth', methods=['POST', 'GET'])
#checks if login information is correct
def auth():
    username = request.form['user']
    password = request.form['pw']
    encrypted = db_builder.encrypt_password(password)
    result = authenticate(username, encrypted)
    if result == SUCCESS:
        session['user'] = username
        flash(session['user'] + " successfully logged in.")
    if result == BAD_PASS:
        flash("Incorrect password.")
    elif result == BAD_USER:
        flash("Incorrect Username.")
    return redirect(url_for('root'))

@app.route('/createaccount', methods=['POST', 'GET'])
#creates an account and runs encryption function on password
def create_account():
    username = request.form['user']
    password = request.form['pw']
    result = check_newuser(username)
    users = db_builder.user_dict()
    if result == SUCCESS:
        db_builder.insertAccount(username,password)
        users[username] = password
        flash(username + " registered.")
    elif result == BAD_USER:
        flash("That username is already in use. Try another one")
        return redirect(url_for('register'))
    return redirect(url_for('root'))


if __name__ == '__main__':
    app.debug = True
    app.run()

