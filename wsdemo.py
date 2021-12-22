from flask import Flask, render_template

app = Flask(__name__)

connected = set()

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/send')
def send():
    return render_template('index_send.html')
