from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login2.html')


if __name__ == '__main__':
    app.run(debug=True)