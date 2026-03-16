from scrapy.crawler import CrawlerProcess

from crawler.settings import *
from crawler.spiders.microcenter import MicrocenterSpider


def run():
    process = CrawlerProcess(settings={
        "BOT_NAME": BOT_NAME,
        "SPIDER_MODULES": SPIDER_MODULES,
        "NEWSPIDER_MODULE": NEWSPIDER_MODULE,
        "ROBOTSTXT_OBEY": ROBOTSTXT_OBEY,
        "ITEM_PIPELINES": ITEM_PIPELINES,
        "LOG_LEVEL": LOG_LEVEL,
        "DOWNLOAD_DELAY": DOWNLOAD_DELAY,
        "CONCURRENT_REQUESTS_PER_DOMAIN": CONCURRENT_REQUESTS_PER_DOMAIN,
        "USER_AGENT": USER_AGENT,
    })
    process.crawl(MicrocenterSpider)
    process.start()


if __name__ == "__main__":
    run()
