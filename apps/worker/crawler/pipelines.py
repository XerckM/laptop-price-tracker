from decimal import Decimal

from crawler.db import SessionLocal


class PostgresPipeline:
    def process_item(self, item, spider):
        db = SessionLocal()

        try:
            # For now, just print so we can confirm scraping flow works
            spider.logger.info(f"Scraped item: {dict(item)}")

            # We will add real DB upsert logic next
            return item

        except Exception:
            db.rollback()
            raise
        finally:
            db.close()
