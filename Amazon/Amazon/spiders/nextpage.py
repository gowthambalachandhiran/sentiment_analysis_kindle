import scrapy
from scrapy.contrib.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from lxml import html

class Scrapy1Spider(scrapy.Spider):
    name = "craiglist"
    allowed_domains = ["www.amazon.com"]
    start_urls = (
        'https://www.amazon.com/Amazon-Kindle-Paperwhite-6-Inch-4GB-eReader/product-reviews/B00OQVZDJM/ref=cm_cr_arp_d_viewopt_rvwer?ie=UTF8&reviewerType=all_reviews&showViewpoints=1&sortBy=helpful&pageNumber=1',
    )

    Rules = (Rule(LinkExtractor(allow=(), restrict_xpaths=('//*[@id="cm_cr-pagination_bar"]/ul/li[8]/a',)), callback="ValueTest", follow= True),)

    def parse(self, response):
        site = html.fromstring(response.body_as_unicode())
        titles = site.xpath('//div[@class="content"]/p[@class="row"]')
        print len(titles), 'AAAA'

        # follow next page links
        next_page = response.xpath('.//*[@id="cm_cr-pagination_bar"]/ul/li[8]/a/@href').extract()
        if next_page:
            next_href = next_page[0]
	    print(next_href)
            next_page_url = 'https://www.amazon.com' + next_href
            request = scrapy.Request(url=next_page_url)
            yield request
