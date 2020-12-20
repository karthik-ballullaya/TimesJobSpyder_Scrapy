from scrapy import Request
from scrapy.spiders import CrawlSpider
from ..items import TimesjoblistingItem


class TimesjobSpider(CrawlSpider):
    name = 'timesjob'
    page_number = 1
    # allowed_domains = ['timesjob.com']
    
    def start_requests(self):        
        keywords       = getattr(self, 'keywords', '')
        location       = getattr(self, 'location', '')
        workexp        = getattr(self, 'workexp', '0')
        self.max_pages = int(getattr(self, 'maxpages', '1'))

        self.base_url = f'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={keywords}&txtLocation={location}&cboWorkExp1={workexp}&sequence='
        print(f'Base url = {self.base_url}')
        yield Request(self.base_url + str(self.page_number), self.parse)
    
    def parse(self, response):
        print('Started parsing')
        item = TimesjoblistingItem()
        jobCards = response.css('.wht-shd-bx')

        if len(jobCards) == 0:
            return

        for jobCard in jobCards:
            jobType         = jobCard.css('h2 a::text').get()
            moreDetails     = jobCard.css('h2 a').attrib['href']
            companyName     = jobCard.css('.joblist-comp-name::text').get()
            reqExp          = jobCard.css('.top-jd-dtl li:nth-child(1)::text').get()
            location        = jobCard.css('.top-jd-dtl span::text').get()
            compensation    = jobCard.css('.top-jd-dtl li:nth-child(2)::text').get() if len(response.css('top-jd-dtl')) else 'NA'
            jobDescription  = jobCard.css('.list-job-dtl li:nth-child(1)::text').getall()
            skillSet        = jobCard.css('.list-job-dtl span.srp-skills::text').getall()
            postedTime      = jobCard.css('.sim-posted span:last-child::text').get()
            isWFHAvailable  = 'Available' if 'Work from Home' in jobCard.css('.sim-posted span:first-child::text').get() else 'NA'
            
            item['jobType'] = jobType
            item['moreDetails'] = moreDetails
            item['companyName'] = companyName
            item['reqExp'] = reqExp
            item['location'] = location
            item['compensation'] = compensation
            item['jobDescription'] = jobDescription
            item['skillSet'] = skillSet
            item['postedTime'] = postedTime
            item['isWFHAvailable'] = isWFHAvailable
            
            yield item
        
        self.page_number += 1
        if self.page_number < self.max_pages:
            next_page = self.base_url + str(self.page_number)
            yield response.follow(next_page, callback = self.parse)
