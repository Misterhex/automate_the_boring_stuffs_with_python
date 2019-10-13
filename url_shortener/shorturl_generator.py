from string import ascii_uppercase, ascii_lowercase
from random import choice
import redis

class InMemoryShortUrlGenerator: 
    
    def __init__(self):
        self.cache = {}
        self.base_url = 'http://localhost:5000'
        digits = ''.join([str(x) for x in range(0, 9)])
        self.choice_permutations = ascii_uppercase + ascii_lowercase + digits

    def generate_short_url(self, url):
        short_url_code = ''.join(choice(self.choice_permutations) for i in range(8))
        short_url = f'{self.base_url}/{short_url_code}'
        self.cache[short_url_code] = url
        return short_url

    def get_original_url_by_code(self, short_url_code):
        return self.cache[short_url_code]

class RedisShortUrlGenerator: 
    
    def __init__(self):
        self.r = redis.Redis(host='localhost', port=6379, db=0)
        self.base_url = 'http://localhost:5000'
        digits = ''.join([str(x) for x in range(0, 9)])
        self.choice_permutations = ascii_uppercase + ascii_lowercase + digits

    def generate_short_url(self, url):
        short_url_code = ''.join(choice(self.choice_permutations) for i in range(8))
        short_url = f'{self.base_url}/{short_url_code}'
        self.r.set(short_url_code, url, ex=5)
        return short_url

    def get_original_url_by_code(self, short_url_code):
        return self.r.get(short_url_code)