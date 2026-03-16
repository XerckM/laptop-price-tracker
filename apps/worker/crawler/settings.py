BOT_NAME = "crawler"

SPIDER_MODULES = ["crawler.spiders"]
NEWSPIDER_MODULE = "crawler.spiders"

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    "crawler.pipelines.PostgresPipeline": 300,
}

LOG_LEVEL = "INFO"

DOWNLOAD_DELAY = 2
CONCURRENT_REQUESTS_PER_DOMAIN = 2

USER_AGENT = "laptop-price-tracker-bot/0.1 (+local development)"
