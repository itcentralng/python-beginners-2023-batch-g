from flask import Flask, render_template

app = Flask(__name__)

@app.get("/")
def index():
    return render_template('home.html')
@app.get('/dashboard')
def dashboard():
    return render_template('dashboard.html')