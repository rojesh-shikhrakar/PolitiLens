import csv
import json
import requests
from bs4 import BeautifulSoup

articles = []

with open('Scraping/links.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
  


    for counter,row in enumerate(csv_reader,1) :
        link = row['Links']
        

        response = requests.get(link)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            title_element = soup.find('div', class_='ok-post-header')
            title = title_element.find('h1').get_text() if title_element else "Title not found"


            date_element = soup.find('span',class_='ok-post-date')
            date = date_element.get_text() if date_element else "Date not found"
            


            article_content = soup.find('div', class_='post-content-wrap')
            article_text = article_content.get_text() if article_content else "News not found"
            
            article_data = {
                'Title' : title,
                'Date' : date,
                'News' :article_text
            }

            articles.append(article_data)
            
            if counter % 100 == 0:
                print(f'Done : {counter} ')

            with open('Scraping/news.json','w',encoding='utf-8') as json_file:
                json.dump(articles, json_file, ensure_ascii=False, indent=4)
            
 