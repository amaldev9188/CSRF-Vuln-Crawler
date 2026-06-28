from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)
username = 'Admin'
password = 'Password'


@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usrn = request.form.get('username', '')
        passwrd = request.form.get('password', '')
        if usrn == username and passwrd == password:
            return redirect(url_for('welcome'))
        return render_template('login.html', error='Invalid Credentials', username=usrn)
    return render_template('login.html')


@app.route('/welcome')
def welcome():
    return render_template('welcome.html', username=username)


if __name__ == '__main__':
    app.run(debug=True)
