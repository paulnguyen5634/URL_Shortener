import random
import string
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# If you want to scale here, you gotta use a database.
shortend_urls = {}


def generate_short_url(length=6):
    chars = string.ascii_letters + string.digits
    # Gets from the chars a random 6 letter/digit combination
    short_url = ''.join(random.choice(chars) for _ in range(length))
    return short_url

# Create an index endpoint
'''
IDEA: 

GET will get the index html file

POST will add a new url
'''
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        long_url = request.form['long_url']
        short_url = generate_short_url()

        while short_url in shortend_urls:
            short_url = generate_short_url()

        shortend_urls[short_url] = long_url
        return f"Shortened URL: {request.url_root}{short_url}"
    
    return render_template('index.html')

@app.route('/<short_url>')
def redirect_url(short_url):
    long_url = shortend_urls.get(short_url)
    if long_url:
        return redirect(long_url)
    else:
        return "URL not found", 404
    
if __name__ == '__main__':
    app.run(debug=True)