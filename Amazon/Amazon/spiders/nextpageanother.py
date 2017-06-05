import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from lxml import html

class Scrapy1Spider(CrawlSpider):
    name = "craiglistanother"
    allowed_domains = ["amazon.com"]
    start_urls = (
        'https://www.amazon.com/Amazon-Kindle-Paperwhite-6-Inch-4GB-eReader/product-reviews/B00OQVZDJM/ref=cm_cr_arp_d_viewopt_rvwer?ie=UTF8&reviewerType=all_reviews&showViewpoints=1&sortBy=helpful&pageNumber=1',
    )

    rules = (Rule(LinkExtractor(allow=(), restrict_xpaths=('//*[@id="cm_cr-pagination_bar"]/ul/li[8]/a',)), callback="parse_page", follow= True),)

    def parse_page(self, response):
        #site = html.fromstring(response.body_as_unicode())
        print('AAAA')
