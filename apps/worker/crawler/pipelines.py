from decimal import Decimal

from sqlalchemy import select

from crawler.db import SessionLocal

# Reuse API models by importing from the API app package
from app.models.offer import Offer
from app.models.price_history import PriceHistory
from app.models.product import Product
from app.models.retailer import Retailer


class PostgresPipeline:
    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        pipeline.crawler = crawler
        return pipeline

    def process_item(self, item):
        db = SessionLocal()

        try:
            data = dict(item)

            retailer = db.execute(
                select(Retailer).where(Retailer.name == data["retailer_name"])
            ).scalar_one_or_none()

            if not retailer:
                retailer = Retailer(
                    name=data["retailer_name"],
                    website=data.get("retailer_website"),
                    is_active=True,
                )
                db.add(retailer)
                db.flush()

            product = db.execute(
                select(Product).where(
                    Product.brand == data["brand"],
                    Product.model == data["model"],
                )
            ).scalar_one_or_none()

            if not product:
                product = Product(
                    brand=data["brand"] or "Unknown",
                    model=data["model"] or data.get("description") or "Unknown Model",
                    sku=data.get("sku"),
                    cpu=data.get("cpu"),
                    gpu=data.get("gpu"),
                    ram_gb=data.get("ram_gb"),
                    ram_type=data.get("ram_type"),
                    ram_speed_mhz=data.get("ram_speed_mhz"),
                    storage_gb=data.get("storage_gb"),
                    storage_type=data.get("storage_type"),
                    storage_interface=data.get("storage_interface"),
                    screen_size=data.get("screen_size"),
                    resolution=data.get("resolution"),
                    panel_type=data.get("panel_type"),
                    refresh_rate_hz=data.get("refresh_rate_hz"),
                    os=data.get("os"),
                    description=data.get("description"),
                )
                db.add(product)
                db.flush()

            offer = db.execute(
                select(Offer).where(
                    Offer.product_id == product.id,
                    Offer.retailer_id == retailer.id,
                    Offer.url == data["url"],
                )
            ).scalar_one_or_none()

            if not offer:
                offer = Offer(
                    product_id=product.id,
                    retailer_id=retailer.id,
                    price=data["price"],
                    currency=data.get("currency", "USD"),
                    url=data["url"],
                    in_stock=data.get("in_stock", True),
                )
                db.add(offer)
                db.flush()
            else:
                offer.price = data["price"]
                offer.currency = data.get("currency", "USD")
                offer.in_stock = data.get("in_stock", True)

            if data.get("price") is not None:
                price_history = PriceHistory(
                    offer_id=offer.id,
                    price=data["price"],
                )
                db.add(price_history)

            db.commit()
            self.crawler.spider.logger.info(
                f"Saved item to DB: {product.brand} {product.model}"
            )

            return item

        except Exception:
            db.rollback()
            raise
        finally:
            db.close()
