from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import csv
from bs4 import BeautifulSoup
import urllib.parse

options = Options()
service = Service(executable_path=r"<path to >\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

with open('keywords.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    keywords = [row[0] for row in reader]

with open('output_data.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Keyword', 'Ad Headline', 'Ad Description', 'Ad URL'])

    for keyword in keywords:
        driver.get("https://www.google.com/search?q=" + keyword)
        driver.implicitly_wait(10)

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        output_data = soup.find_all('div', {'class': 'uEierd'})
        
        for ad in output_data:
            ad_url = ad.find('a')['href']
            parsed_url = urllib.parse.urlparse(ad_url)
            if parsed_url.netloc == 'www.googleadservices.com':
                ad_url = urllib.parse.parse_qs(parsed_url.query)['adurl'][0]
            elif parsed_url.path == '/aclk':
                ad_params = urllib.parse.parse_qs(parsed_url.query)
                try:
                    ad_url = urllib.parse.unquote(ad_params['adurl'][0])
                except KeyError:
                    try:
                        ad_url = urllib.parse.unquote(ad_params['url'][0])
                    except KeyError:
                        continue
            ad_headline = ad.find('div', {'class': 'CCgQ5'})
            if ad_headline:
                ad_headline_text = ad_headline.text
                ad_description = ad.find('div', {'class': 'yDYNvb'}).text
                writer.writerow([keyword, ad_headline_text, ad_description, ad_url])

driver.quit()
