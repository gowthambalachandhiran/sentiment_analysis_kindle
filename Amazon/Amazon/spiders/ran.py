import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from Amazon.items import AmazonItem


class QuotesSpider(scrapy.Spider):
    name = "oldamareview"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/tag/humor/page/1/',
            'http://quotes.toscrape.com/tag/humor/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        #questions = Selector(response).xpath('/html/body/div/div[2]/div[1]')        
        
        for quote in response.xpath("/html/body/div/div[2]/div[1]/div"):
            text = quote.xpath("span[@class='text']/text()").extract_first()
            author = quote.css("small.author::text").extract_first()
            tags = quote.css("div.tags a.tag::text").extract()
            print(text)
            print(author)
            print(tags)
        #for question in questions:
            #print(question.xpath('div/span/text()').extract()) 
            #print("\n=========================================\n")


