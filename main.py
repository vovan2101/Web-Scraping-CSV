import requests
from bs4 import BeautifulSoup
import json
import csv


# url = requests.get('https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie')

# soup = BeautifulSoup(url.text, 'lxml')
# all_products_hrefs = soup.find_all(class_ = 'mzr-tc-group-item-href')


# all_categories_dict = {}
# for item in all_products_hrefs:
#     item_text = item.text
#     item_href = 'https://health-diet.ru' + item.get('href')
    
#     all_categories_dict[item_text] = item_href

# with open('all_categories_dics.json', 'w', encoding='utf-8') as file:
#     json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)

with open('all_categories_dics.json', encoding='utf-8') as file:
    all_categories = json.load(file)


for category_name, category_href in all_categories.items():

    rep = [',', ' ', '-', "'"]
    for item in rep:
        if item in category_name:
            category_name = category_name.replace(item, '_')
    
    req = requests.get(url=category_href)
    soup = BeautifulSoup(req.text, 'lxml')

    table_head = soup.find(class_ = 'uk-table mzr-tc-group-table uk-table-hover uk-table-striped uk-table-condensed').find('tr').find_all('th')
    product = table_head[0].text
    calories = table_head[1].text
    proteins = table_head[2].text
    fats = table_head[3].text
    carbohydrates = table_head[4].text
    

    # saving product categories in csv file
    with open(f'{category_name}.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(
            (
              product,
              calories,
              proteins,
              fats,
              carbohydrates
            )
        )
    
    # Getting all data about products
    products_data = soup.find(class_ = 'mzr-tc-group-table').find('tbody').find_all('tr')

    for item in products_data:
        product_tds = item.find_all('td')

        title = product_tds[0].find('a').text
        calories = product_tds[1].text
        proteins = product_tds[2].text
        fats = product_tds[3].text
        carbohydrates = product_tds[4].text
        