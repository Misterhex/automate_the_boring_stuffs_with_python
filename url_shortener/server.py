from flask import Flask
from flask import request
from flask import redirect
from shorturl_generator import InMemoryShortUrlGenerator, RedisShortUrlGenerator
app = Flask(__name__)

short_url_generator = RedisShortUrlGenerator()

@app.route('/_generate_short_url', methods=['POST'])
def shorten_url():
    json_body = request.get_json()
    original_url = json_body['url']
    print(original_url)
    short_url  = short_url_generator.generate_short_url(original_url)
    return short_url

@app.route('/<short_url_code>')
def redirect_short_url(short_url_code):
    original_url = short_url_generator.get_original_url_by_code(short_url_code)
    return redirect(original_url, code=301)