import scrapy
import re
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals

class WebsiteScrapper(scrapy.Spider):
    name = "websitesdata"

    start_urls = [
        'https://www.analyticsvidhya.com/blog/',
        'http://www.bigdatanews.com',
        'http://www.rdatamining.com',
        'https://www.oracle.com'
        'https://www.khanacademy.org'
        'https://www.datasciencecentral.com'
        'https://www.analytics-magazine.org'
    ]

    seed_words = []
    links = []
    visited_links = []
    max_level = 200

    level = 0
    count_vectors = {}
    out = open("scrapedData.txt","w")

    def __init__(self, *args, **kwargs):
        dispatcher.connect(self.spider_closed, signal=signals.spider_closed)
        self.seed_words = [word.strip(" \n") for word in(open("seed words.txt").readlines())]
        print "Seed Words ::::"+str(self.seed_words)
        super(WebsiteScrapper, self).__init__(*args, **kwargs)

    def count_seed_words(self, text=""):
        vector = {}
        """for word in text.split():
            if word in self.seed_words:
                if not word in vector.keys():
                    vector[word]=1
                else:
                    vector[word] = vector[word]+1
        """
        for word in self.seed_words:
            count = len(re.findall(word,text))
            if not word in vector.keys():
                vector[word] = count
            else:
                vector[word] = vector[word] + count
        return vector

    def join_dict(self,original={},update={}):
        for key in update.keys():
            if key in original.keys():
                original[key] = original[key]+update[key]
            else:
                original[key] = update[key]
        return original

    def parse(self, response):
        if self.level<self.max_level:
            self.level=self.level+1
            self.visited_links.append(response.url)
            cur_url = response.url.split("//")[1].split("/")[0]
            content = response.css("p::text").extract_first()
            if content is not None:
                content = response.css("p::text").extract()
                content = [line.encode('utf-8') for line in content]
                for line in content:
                    if not cur_url in self.count_vectors.keys():
                        self.count_vectors[cur_url] = self.count_seed_words(line)
                    else:
                        vector = self.count_seed_words(line)
                        self.count_vectors[cur_url] = self.join_dict(self.count_vectors[cur_url], vector)

            next_links = response.css("a::attr(href)").extract()
            for link in next_links:
                if not link in self.links:
                    self.links.append(link)
            #print next_links
            for link in next_links:
                if not link in self.visited_links and len(link)>1:
                    yield scrapy.Request(link,callback=self.parse)

    def spider_closed(self,spider):
        print "Closing spider"
        self.out.write(str(self.count_vectors))
        self.out.close()