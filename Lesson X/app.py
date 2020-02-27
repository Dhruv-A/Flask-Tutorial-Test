from flask import Flask, render_template, redirect

app = Flask(__name__)
@app.route('/')
def mainpage():
    return render_template('home.html')


@app.route('/home')
def home():
    return redirect('/')


@app.route('/about')
def abouts():
    return render_template('about.html')


app.run(debug='true')
