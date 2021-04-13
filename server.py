from flask import Flask, render_template, flash, request, redirect, url_for
import random

app = Flask(__name__)
    

@app.route('/')
def index():
    return render_template('index.html', link = 'https://s3.amazonaws.com/nuclearlaunchdetected/mp3/Carrier_Attack00.mp3')

@app.route('/playAudio', methods=['GET'])
def playAudio():
    links = []
    with open('links.txt') as f:
        links = f.readlines()
    link = random.choice(links)
    print(link)
    return render_template('index.html', link = link)

if __name__ == '__main__':
    app.run(debug=False, host = '127.0.0.1')