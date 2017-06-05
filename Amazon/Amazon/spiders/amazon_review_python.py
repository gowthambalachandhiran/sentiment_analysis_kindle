import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from lxml import html
from scrapy import Spider
from scrapy.selector import Selector
#from Amazon.items import AmazonItem


class QuotesSpider(scrapy.Spider):
    name = "amareviewtest"
    allowed_domains = ["www.amazon.in"]
    def start_requests(self):
        #urls = []
        #for num in range(1,10):
            #urls.append('https://www.amazon.com/Amazon-Kindle-Paperwhite-6-Inch-4GB-eReader/product-reviews/B00OQVZDJM/ref=cm_cr_arp_d_viewopt_rvwer?ie=UTF8&reviewerType=all_reviews&showViewpoints=1&sortBy=helpful&pageNumber=%d'%(num))
	#print(urls)
	urls=['https://www.amazon.com/Amazon-Kindle-Paperwhite-6-Inch-4GB-eReader/product-reviews/B00OQVZDJM/ref=cm_cr_arp_d_viewopt_rvwer?ie=UTF8&reviewerType=all_reviews&showViewpoints=1&sortBy=helpful&pageNumber=1']
	for num in range(2,5):
	    urls.append('https://www.amazon.com/Amazon-Kindle-Paperwhite-6-Inch-4GB-eReader/product-reviews/B00OQVZDJM/ref=cm_cr_arp_d_paging_btm_'+str(num)+'?ie=UTF8&pageNumber='+str(num)+'&reviewerType=all_reviews&sortBy=helpful')
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
	print("--------------------Page--------------------")
        #questions = Selector(response).xpath('/html/body/div/div[2]/div[1]')        
        #print(response.xpath('//*[@id="cm_cr-review_list"]/div[1]/div/div[1]/a[1]/i/span/text()').extract_first())	
        for onediv in response.xpath('//*[@id="cm_cr-review_list"]/div'):
	    #item = AmazonItem()
            val = onediv.xpath('div/div[1]/a[1]/i/span/text()').extract_first()
	    if(val):
		print("MANIVANNAN SHGFGHWSHJGVSD JHVDHGSVHG")
		#item['Star'] = val
                #item['Title'] = onediv.xpath('div/div[1]/a[2]/text()').extract_first()
	  	#item['User'] = onediv.xpath('div/div[2]/span[1]/a/text()').extract_first()
		#item['Date'] = onediv.xpath('div/div[2]/span[4]/text()').extract_first()
		#item['Color'] = onediv.xpath('div/div[3]/a/text()').extract()[0].split(": ",1)[1]
		#item['Connectivity'] = onediv.xpath('div/div[3]/a/text()').extract()[1].split(": ",1)[1]
		#item['Offer_type'] = onediv.xpath('div/div[3]/a/text()').extract()[2].split(": ",1)[1]
		strval = onediv.xpath('div/div[4]/span/text()').extract()
                str = ""
                for te in strval:
                   str +=te
                #item['Review'] = str
		print(str)
                print("=============================================")	   
                #yield item


