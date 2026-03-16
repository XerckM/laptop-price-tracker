import scrapy


class LaptopOfferItem(scrapy.Item):
    retailer_name = scrapy.Field()
    retailer_website = scrapy.Field()

    brand = scrapy.Field()
    model = scrapy.Field()
    sku = scrapy.Field()

    cpu = scrapy.Field()
    gpu = scrapy.Field()

    ram_gb = scrapy.Field()
    ram_type = scrapy.Field()
    ram_speed_mhz = scrapy.Field()

    storage_gb = scrapy.Field()
    storage_type = scrapy.Field()
    storage_interface = scrapy.Field()

    screen_size = scrapy.Field()
    resolution = scrapy.Field()
    panel_type = scrapy.Field()
    refresh_rate_hz = scrapy.Field()

    os = scrapy.Field()
    description = scrapy.Field()

    price = scrapy.Field()
    currency = scrapy.Field()
    url = scrapy.Field()
    in_stock = scrapy.Field()
