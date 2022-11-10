import requests
from bs4 import BeautifulSoup
import lxml
import json

headers = {
    'user-agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36'
}

# for i in range(0, 96, 24):
for i in range(0, 24, 24):
    url = f'https://www.skiddle.com/festivals/search/?ajaxing=1&sort=0&fest_name=&from_date=9%20Nov%202022&to_date=&where%5B%5D=2&where%5B%5D=3&where%5B%5D=4&maxprice=500&o={i}&bannertitle=May'
    
    req = requests.get(url=url, headers=headers)
    json_data = json.loads(req.text)
    html_response = json_data['html']

    with open(f'index_{i}.html', 'w') as file:
        file.write(html_response)