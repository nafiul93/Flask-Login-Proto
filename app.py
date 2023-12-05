from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the login prototype.'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Perform authentication (you can replace this with your authentication logic)

        # For demonstration purposes, let's just check if the username is "admin" and password is "password"
        if username == 'admin' and password == 'password':
            return 'Login successful!'
        else:
            return 'Login failed. Please check your username and password.'

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
