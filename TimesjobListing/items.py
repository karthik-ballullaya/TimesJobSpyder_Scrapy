# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TimesjoblistingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    jobType         = scrapy.Field()
    moreDetails     = scrapy.Field()
    companyName     = scrapy.Field()
    reqExp          = scrapy.Field()
    location        = scrapy.Field()
    compensation    = scrapy.Field()
    jobDescription  = scrapy.Field()
    skillSet        = scrapy.Field()
    postedTime      = scrapy.Field()
    isWFHAvailable  = scrapy.Field()
    
