from flask import Flask, render_template, request, redirect, flash, session

app = Flask(__name__)

app.secret_key = "sdjfhsdkjfhsjdkhfjksdh"


database = []

@app.get("/")
def index():
    return render_template('register.html')

@app.post("/")
def index2():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    data = {"name":name, "email":email, "password":password, "id":len(database)+1, 'avatar':"{}.jpg".format(len(database)+1)}
    database.append(data)
    return redirect('/login')

@app.get("/login")
def login():
    return render_template('login.html')

@app.post("/login")
def login2():
    email = request.form.get('email')
    password = request.form.get('password')
    for data in database:
        if data.get('email') == email and data.get('password') == password:
            session['user'] = data
            return redirect('/dashboard')
    flash("Wrong credentials, please try again!")
    return render_template('login.html')

@app.get('/dashboard')
def dashboard():
    return render_template('dashboard.html')