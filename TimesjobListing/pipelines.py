# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3
import re
from .items import TimesjoblistingItem
from itemadapter import ItemAdapter


class TimesjoblistingDBPipeline:
    
    def open_spider(self, spider):
        self.create_connection()
        self.create_table()
        
    def close_spider(self, spider):
        self.close_connection()
    
    def create_connection(self):
        self.conn = sqlite3.connect("JobListing.db")
        self.curr = self.conn.cursor()
        
    def create_table(self):
        self.curr.execute('''DROP TABLE IF EXISTS job_listing_tb''')
        self.curr.execute('''create table job_listing_tb(
                            jobType text,
                            moreDetails text,
                            companyName text,
                            reqExp text,
                            location text,
                            compensation text,
                            jobDescription text,
                            skillSet text,
                            postedTime text,
                            isWFHAvailable text
                            )''')

    def close_connection(self):
        self.conn.close()
    
    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
       self.curr.execute('''insert into job_listing_tb values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (
                           item['jobType'],
                           item['moreDetails'],
                           item['companyName'],
                           item['reqExp'],
                           item['location'],
                           item['compensation'],
                           item['jobDescription'],
                           item['skillSet'],
                           item['postedTime'],
                           item['isWFHAvailable']
                           ))
       self.conn.commit()
       
       
class TimesjoblistingTextCleanPipeline:
    
    cleanText = lambda self, x: re.sub(r'[\n\r\t]*', '', x)
        
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        for key in TimesjoblistingItem.fields.keys():
            if type(adapter[key]) == list:
                adapter[key] = ''.join(adapter[key])
            adapter[key] = self.cleanText(adapter[key])
        return item
