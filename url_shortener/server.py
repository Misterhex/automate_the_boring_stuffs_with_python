from flask import Flask
from flask import request
from flask import redirect
from random import choice
from string import ascii_uppercase
import urllib
app = Flask(__name__)

base_url = 'http://localhost:5000'
cache = {}

class ShortUrlGenerator: 

    def generate_short_url(self, url):
        short_url_code = ''.join(choice(ascii_uppercase) for i in range(8))
        short_url = f'{base_url}/{short_url_code}'
        cache[short_url_code] = url
        return short_url

@app.route('/_generate_short_url', methods=['POST'])
def shorten_url():
    json_body = request.get_json()
    original_url = json_body['url']
    print(original_url)
    short_url  = ShortUrlGenerator().generate_short_url(original_url)
    return short_url

@app.route('/<short_url_code>')
def redirect_short_url(short_url_code):
    return redirect(cache[short_url_code],code=301)