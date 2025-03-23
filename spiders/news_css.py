import scrapy
from lab2.items import NewsItem


class NewsSpider(scrapy.Spider):
    name = "news_css"
    allowed_domains = ["radiosvoboda.org"]
    start_urls = ["https://www.radiosvoboda.org/z/630"]

    def parse(self, response):
        count = 1
        items = response.css('div.media-block')

        for item in items:
            print(count)
            count += 1
            title = item.css('h4::text').get()
            url = item.css('a::attr(href)').get()
            date = item.css('span::text').get()
            img_url = item.css('img::attr(src)').get()
            yield NewsItem(title=title, url=url, date=date, img_url=img_url)
