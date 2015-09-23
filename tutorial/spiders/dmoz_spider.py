import scrapy

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["glassdoor.com"]
    S = ["http://www.glassdoor.com/Interview/Google-Interview-Questions-E9079_P"+str(x)+".htm?sort.sortType=RD&sort.ascending=false&filter.jobTitleFTS=software+engineer" for x in xrange(1,200)]
    start_urls = S

    def parse(self, response):

        for sel in response.xpath('//div[@class="interviewQuestions margBot notranslate"]'):
            desc = sel.xpath('.//ul/li/span/text()').extract()
            with open('log.txt', 'a') as f:
                f.write(str(desc)+"\n")

