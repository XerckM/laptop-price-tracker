from crawler.db import SessionLocal


class PostgresPipeline:
    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        pipeline.crawler = crawler
        return pipeline

    def process_item(self, item):
        db = SessionLocal()

        try:
            self.crawler.spider.logger.info(f"Scraped item: {dict(item)}")
            return item
        except Exception:
            db.rollback()
            raise
        finally:
            db.close()
