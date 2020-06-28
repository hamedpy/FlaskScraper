from flask import Flask, render_template, url_for, redirect, request, flash
import secrets
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(5) 
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        urlinput = request.form['urlinput']
        try:
            req = requests.get(urlinput)
            return req.text
        except requests.exceptions.MissingSchema:
            flash('just enter the URL')
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug = True)
