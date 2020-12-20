# TimesJobSpyder_Scrapy
A spyder bot to scrape timesjob.com for job listings and save in a db using scrapy

## Table of contents:
1. [Installation](installation)
2. [Scraped details](data-scraped)
3. [How to run the spyder](how-to-run)
4. [How to view the results](how-to-view-the-results)

### Installation:
run the following command to install the packages: pip install -r requirements.txt

### Data scraped:
The spyder scrapes these following fields:

|      Field     | Datatype |                   Description                  |
|:--------------:|:--------:|:----------------------------------------------:|
| jobType        | string   | Type of job                                    |
| moreDetails    | string   | href to get more details about the job listing |
| companyName    | string   | Name of the company                            |
| reqExp         | string   | Required experience                            |
| location       | string   | Location of office                             |
| compensation   | string   | Compensation for the job                       |
| jobDescription | string   | Description of the job                         |
| skillSet       | string   | Skill set required for the job                 |
| postedTime     | string   | When was the job listed                        |
| isWFHAvailable | string   | Is Work from home option available             |

### How to run:
Ex Cmd: scrapy crawl timesjob -a keywords="Data science" -a location="Mumbai" -a workexp="1" -a maxpages="100"

### How to view the results:
The scraped details is stored in a sqlite database. One can use [sqliteonline](https://sqliteonline.com/) for quick viewing of the database.

ex cmd: SELECT * FROM job_listing_tb;

To view all the entries
