import scrapy

from crawler.items import LaptopOfferItem


class MicrocenterSpider(scrapy.Spider):
    name = "microcenter"
    allowed_domains = ["microcenter.com"]

    start_urls = [
        "https://www.microcenter.com/search/search_results.aspx?N=4294967288+4294807523"
    ]

    custom_headers = {
        "Referer": "https://www.microcenter.com/",
    }

    async def start(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url=url,
                headers=self.custom_headers,
                callback=self.parse,
                dont_filter=True,
            )

    def parse(self, response):
        self.logger.info(f"Fetched {response.url} with status {response.status}")

        if response.status != 200:
            self.logger.warning(f"Non-200 response received: {response.status}")
            return

        product_cards = response.css("li.product_wrapper")

        if not product_cards:
            self.logger.warning("No product cards found. Selector likely needs adjustment.")
            self.logger.info(response.text[:1500])
            return

        for card in product_cards[:5]:
            title = card.css("h2 a::text").get()
            url = card.css("h2 a::attr(href)").get()
            price = card.css(".price span::text").get()

            item = LaptopOfferItem()

            item["retailer_name"] = "Micro Center"
            item["retailer_website"] = "https://www.microcenter.com"

            item["brand"] = None
            item["model"] = title.strip() if title else None
            item["sku"] = None

            item["cpu"] = None
            item["gpu"] = None

            item["ram_gb"] = None
            item["ram_type"] = None
            item["ram_speed_mhz"] = None

            item["storage_gb"] = None
            item["storage_type"] = None
            item["storage_interface"] = None

            item["screen_size"] = None
            item["resolution"] = None
            item["panel_type"] = None
            item["refresh_rate_hz"] = None

            item["os"] = None
            item["description"] = title.strip() if title else None

            item["price"] = price.strip() if price else None
            item["currency"] = "USD"

            item["url"] = response.urljoin(url) if url else None
            item["in_stock"] = True

            yield item
