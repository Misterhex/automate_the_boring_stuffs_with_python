import requests
import bs4

proxies = {
  "http": None,
  "https": None,
}

response = requests.get('https://www.hackthissite.org/', proxies=proxies)

print(response.status_code)

soup_obj = bs4.BeautifulSoup(response.text,'lxml')

links = soup_obj.find_all('a')

for link in links:
    print(link.get('href'))