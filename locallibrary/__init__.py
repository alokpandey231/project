import scrapy
import re
from scrapy.spiders import XMLFeedSpider
from lifescience.items import LifescienceItem,SeekingalphaItem
#from BioCentury RSS
class Spider(XMLFeedSpider,scrapy.Spider):
    name = "pharmiweb"
    allowed_domains = ['www.pharmiweb.com']
    start_urls = ['https://www.pharmiweb.com/rss/press-releases'] #Crawl
    itertag = 'item'

    def parse_node(self, response, node):
        #self.logger.info('Hi, this is a <%s> node!: %s', self.itertag, ''.join(node.getall()))

        item = LifescienceItem()
        item['title'] = node.xpath('title/text()',).extract_first()                #define XPath for title
        item['link'] = node.xpath('link/text()').extract_first()
        item['pubDate'] = node.xpath('pubDate/text()').extract_first()
        item['description'] = node.xpath('description/text()').extract_first()
        nextpage = response.urljoin(node.xpath('link/text()').extract_first())
        #self.logger.info('Hi, this is a <%s>', (item['link']).strip(),)
        nextpage = item['link'].strip()
        #print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        #print(nextpage)
        request =  scrapy.Request(nextpage, callback=self.parse_child, dont_filter=True, errback=self.err_fun)

        request.meta['item'] = item.copy() #By calling .meta, we can pass our item object into the callback.
        yield request

    def parse_child(self, response):
        #print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
        item = response.meta['item'] #Get the item we passed from scrape()
        item['detail'] = (' '.join(response.xpath('/html/body/main/div/div/div/div/div[1]/section/div[2]/div//text()').getall())).encode('ascii', 'ignore')
        item['author'] = response.xpath('/html/body/main/div/div/div/div/div[1]/section/div[3]/div/div/div[1]/div/ul/li/ul/li//text()').extract_first()
        #self.logger.info('Hi,  <%s>', item,)
        yield item #Return the new phonenumber'd item back to scrape


    def err_fun(self, failure):
        print("IN ERRORRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR", failure)

class Spider(XMLFeedSpider,scrapy.Spider):
    name = "drugs"
    allowed_domains = ['www.drugs.com']
    start_urls = ['https://www.drugs.com/feeds/medical_news.xml','https://www.drugs.com/feeds/headline_news.xml','https://www.drugs.com/feeds/clinical_trials.xml','https://www.drugs.com/feeds/fda_alerts.xml','https://www.drugs.com/feeds/new_drug_approvals.xml','https://www.drugs.com/feeds/new_drug_applications.xml'] #Crawl
    itertag = 'item'

    def parse_node(self, response, node):
        #self.logger.info('Hi, this is a <%s> node!: %s', self.itertag, ''.join(node.getall()))

        item = LifescienceItem()
        item['title'] = node.xpath('title/text()',).extract_first()             #define XPath for title
        item['link'] = node.xpath('link/text()').extract_first()
        item['pubDate'] = node.xpath('pubDate/text()').extract_first()
        item['description'] = node.xpath('description/text()').extract_first()
        nextpage = response.urljoin(node.xpath('link/text()').extract_first())
        self.logger.info('Hi, this is a <%s>', (item['link']).strip(),)
        nextpage = item['link'].strip()
        #print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        #print(nextpage)
        request =  scrapy.Request(nextpage, callback=self.parse_child, dont_filter=True, errback=self.err_fun)

        request.meta['item'] = item.copy() #By calling .meta, we can pass our item object into the callback.
        yield request

    def parse_child(self, response):
        #print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
        item = response.meta['item'] #Get the item we passed from scrape()
        item['detail'] = (' '.join(response.xpath('/html/body/div/div[1]/div[2]/div/div[1]/div[2]/p//text()').getall())).encode('ascii', 'ignore')
        item['author'] = 'None'
        #self.logger.info('Hi,  <%s>', item,)
        yield item #Return the new phonenumber'd item back to scrape


    def err_fun(self, failure):
        print("IN ERRORRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR", failure)

class Spider(XMLFeedSpider,scrapy.Spider):
    name = "fiercepharma"
    allowed_domains = ['www.fiercepharma.com']
    start_urls = ['https://www.fiercepharma.com/rss/xml'] #Crawl
    itertag = 'item'

    def parse_node(self, response, node):
        #self.logger.info('Hi, this is a <%s> node!: %s', self.itertag, ''.join(node.getall()))

        item = LifescienceItem()
        item['title'] = node.xpath('title/text()',).extract_first()                #define XPath for title
        item['link'] = node.xpath('link/text()').extract_first()
        item['pubDate'] = node.xpath('pubDate/text()').extract_first()
        item['description'] = node.xpath('description/text()').extract_first()
        nextpage = response.urljoin(node.xpath('link/text()').extract_first())
        #self.logger.info('Hi, this is a <%s>', (item['link']).strip(),)
        nextpage = item['link'].strip()
        #print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        #print(nextpage)
        request =  scrapy.Request(nextpage, callback=self.parse_child, dont_filter=True, errback=self.err_fun)

        request.meta['item'] = item.copy() #By calling .meta, we can pass our item object into the callback.
        yield request

    def parse_child(self, response):
        #print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
        item = response.meta['item'] #Get the item we passed from scrape()
        item['detail'] = (' '.join(response.xpath('/html/body/div[1]/div[1]/div[2]/main/div[2]/div[2]/div[2]/article/div[3]/div[2]/div[1]/p//text()').getall())).encode('ascii', 'ignore')
        item['author'] = response.xpath('/html/body/div[1]/div[1]/div[2]/main/div[2]/div[2]/div[2]/article/footer/div/a//text()').extract_first()
        #self.logger.info('Hi,  <%s>', item,)
        yield item #Return the new phonenumber'd item back to scrape


    def err_fun(self, failure):
        print("IN ERRORRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR", failure)


class Spider(XMLFeedSpider,scrapy.Spider):
    name = "biom"
    allowed_domains = ['www.bio-medicine.org']
    start_urls = ['http://www.bio-medicine.org/inc/biomed/medicine-technology.asp','http://www.bio-medicine.org/inc/biomed/medicine-news.asp','http://www.bio-medicine.org/inc/biomed/biology-technology.asp','http://www.bio-medicine.org/inc/biomed/biology-news.asp'] #Crawl
    itertag = 'item'

    def parse_node(self, response, node):
        #self.logger.info('Hi, this is a <%s> node!: %s', self.itertag, ''.join(node.getall()))

        item = LifescienceItem()
        item['title'] = node.xpath('title/text()',).extract_first()                #define XPath for title
        item['link'] = node.xpath('link/text()').extract_first()
        item['pubDate'] = node.xpath('pubDate/text()').extract_first()
        item['description'] = (re.sub(' {2,}', ' ', node.xpath('description/text()').extract_first())).encode('ascii', 'ignore')
        nextpage = response.urljoin(node.xpath('link/text()').extract_first())
        #self.logger.info('Hi, this is a <%s>', (item['link']).strip(),)
        nextpage = item['link'].strip()
        #print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        #print(nextpage)
        request =  scrapy.Request(nextpage, callback=self.parse_child, dont_filter=True, errback=self.err_fun)

        request.meta['item'] = item.copy() #By calling .meta, we can pass our item object into the callback.
        yield request

    def parse_child(self, response):
        #print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
        item = response.meta['item'] #Get the item we passed from scrape()
        item['detail'] = re.sub(' {2,}', ' ', (' '.join(response.xpath('//*[@id="bx_sen"]/p//text()').getall())).encode('ascii', 'ignore'))
        item['author'] = response.xpath('/html/body/div/div[4]/div[3]/div[4]/table/tr/td[1]/a//text()').extract_first()
        #self.logger.info('Hi,  <%s>', item,)
        yield item #Return the new phonenumber'd item back to scrape


    def err_fun(self, failure):
        print("IN ERRORRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR", failure)
class Spider(XMLFeedSpider,scrapy.Spider):
    name = "seekingalpha"
    allowed_domains = ['']
    start_urls = ['https://seekingalpha.com/market_currents.xml'] #Crawl
    itertag = 'item'

    def parse_node(self, response, node):
        #self.logger.info('Hi, this is a <%s> node!: %s', self.itertag, ''.join(node.getall()))

        item = SeekingalphaItem()
        item['title'] = node.xpath('title/text()',).extract_first()                #define XPath for title
        item['link'] = node.xpath('link/text()').extract_first()
        item['catog'] = node.xpath('category/text()').extract_first()
        nextpage = response.urljoin(node.xpath('link/text()').extract_first())
        #self.logger.info('Hi, this is a <%s>', (item['link']).strip(),)
        nextpage = item['link'].strip()
        #print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        #print(nextpage)
        request =  scrapy.Request(nextpage, callback=self.parse_child, dont_filter=True, errback=self.err_fun)

        request.meta['item'] = item.copy() #By calling .meta, we can pass our item object into the callback.
        yield request

    def parse_child(self, response):
        #print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
        item = response.meta['item'] #Get the item we passed from scrape()
        item['description'] = re.sub(' {2,}', ' ', (' '.join(response.xpath('//*[@id="bullets_ul"]//text()').getall())).encode('ascii', 'ignore'))
        item['author'] = response.xpath('/html/body/div[1]/div/div[1]/div[2]/article/header/div[4]/span[3]/a/span//text()').extract_first()
        #self.logger.info('Hi,  <%s>', item,)
        yield item #Return the new phonenumber'd item back to scrape


    def err_fun(self, failure):
        print("IN ERRORRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR", failure)
