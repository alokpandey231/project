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
import urllib2
from lxml import etree as ET
#reddit parse
from dateutil.parser import parse

def is_date(string, fuzzy=False):
    try:
        return parse(string, fuzzy=True)

    except ValueError:
        return False

def get_itertag(url):
    print url
    def most_frequent(List):
        counter = 0
        num = List[0]

        for i in List:
            curr_frequency = List.count(i)
            if(curr_frequency> counter):
                counter = curr_frequency
                num = i

        if counter >1:
            return num

        else:
            return None

    site = url
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'}
    req = urllib2.Request(site, headers=headers)
    reddit_file = urllib2.urlopen(req)
    #
    #entire feed
    tree =  ET.ElementTree(file = reddit_file)
    print (reddit_file.read())

    ############## get the root node
    root = (tree.getroot())
    print ("root",root.tag)
    x = [ child.tag for child in root ]
    print(x)
    ######  there can be multiple notes till the main node
    if len(x) == 1:
        x = root.find(x[0])
    #subchild = ET.Element('channel')
    #getchildren
        tags = [ child.tag for child in x ]

    else:
        print "more thann one node"
        x = root
        tags = [ child.tag for child in x ]
    #######################################################################################

    print (list(tags))
    max_data = most_frequent(tags)
    print (max_data,"max data ")
    print (list(x.find(max_data)))
    if max_data is not None and len(list(x.find(max_data))) > 0:
        print ("in if")
        if len([ child.tag for child in x.find(max_data) ]) > 1:
            itertag= max_data

    else:
        print ("in else")
        for child in x:
            if len(list(child)) > 1:
                itertag = child.tag

    data_node = x.findall(str(itertag))
    print ((data_node))
    for i in data_node:
        for data in i:
	    
            try:
		print data.text
                text =  (data.text).strip()
                if (text.startswith('https://') or text.startswith('http://')):
                    print "link",text
                elif len(text) < 100:
                    date = is_date(text)
                    if  date is not False:
                        print "date",date
            except:
                print ("error in data",data)
                try:
                    link =  data.attrib['href']
                    print "link",link
                except:
                    pass


urls = ['https://www.pharmiweb.com/rss/press-releases','https://www.drugs.com/feeds/medical_news.xml','https://www.drugs.com/feeds/headline_news.xml','https://www.drugs.com/feeds/clinical_trials.xml','https://www.drugs.com/feeds/fda_alerts.xml','https://www.drugs.com/feeds/new_drug_approvals.xml','https://www.drugs.com/feeds/new_drug_applications.xml','https://www.fiercepharma.com/rss/xml','http://www.bio-medicine.org/inc/biomed/medicine-technology.asp','http://www.bio-medicine.org/inc/biomed/medicine-news.asp','http://www.bio-medicine.org/inc/biomed/biology-technology.asp','http://www.bio-medicine.org/inc/biomed/biology-news.asp','https://seekingalpha.com/market_currents.xml','https://www.pharmiweb.com/rss/press-releases','http://www.appliedclinicaltrialsonline.com/sitefeed/2568']
print (len(urls))
#iter_tag = []
#for url in urls:
#    data = get_itertag(url)

print ("itertag",get_itertag('http://www.appliedclinicaltrialsonline.com/sitefeed/2568'))
#print ("itertag",iter_tag)
