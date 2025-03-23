import scrapy
from lab2.items import NewsItem


class NewsSpider(scrapy.Spider):
    name = "news_xpath"
    allowed_domains = ["radiosvoboda.org"]
    start_urls = ["https://www.radiosvoboda.org/z/630"]

    def parse(self, response):
        count = 1
        items = response.xpath('//div[contains(@class, "media-block")]')

        for item in items:
            print(count)
            count += 1
            title = item.xpath('.//h4/text()').get()
            url = item.xpath('.//a/@href').get()
            date = item.xpath('.//span/text()').get()
            img_url = item.xpath('.//img/@src').get()
            yield NewsItem(title=title, url=url, date=date, img_url=img_url)
