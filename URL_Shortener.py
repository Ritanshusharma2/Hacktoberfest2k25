#Project Title: Python URL Shortener

from flask import Flask, request, render_template
import requests

app = Flask(__name__)

BITLY_ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'

@app.route('/', methods=['GET', 'POST'])
def home():
    short_url = ''
    if request.method == 'POST':
        long_url = request.form['long_url']
        headers = {'Authorization': f'Bearer {BITLY_ACCESS_TOKEN}'}
        data = {'long_url': long_url}
        response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, json=data)
        if response.status_code == 200:
            short_url = response.json().get('link')
    return render_template('index.html', short_url=short_url)

if __name__ == '__main__':
    app.run(debug=True)
