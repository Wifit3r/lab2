import scrapy
from bs4 import BeautifulSoup
from lab2.items import NewsItem


class NewsSpider(scrapy.Spider):
    name = "news"
    allowed_domains = ["radiosvoboda.org"]
    start_urls = ["https://www.radiosvoboda.org/z/630"]

    def parse(self, response):
        soup = BeautifulSoup(response.body, 'html.parser')
        count = 1
        items = soup.find_all('div', class_='media-block')
        for item in items:
            print(count)
            count += 1
            Title = item.find('h4').text
            url = item.find('a')['href']
            date = item.find('span').text
            img_url = item.find('img')['src']
            yield NewsItem(Title=Title, url=url, date=date, img_url=img_url)
