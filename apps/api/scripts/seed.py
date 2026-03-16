from decimal import Decimal

from app.core.database import SessionLocal
from app.models.offer import Offer
from app.models.price_history import PriceHistory
from app.models.product import Product
from app.models.retailer import Retailer


def seed_database() -> None:
    db = SessionLocal()

    try:
        # Prevent duplicate seeding
        existing_product = db.query(Product).first()
        if existing_product:
            print("Seed data already exists. Skipping.")
            return

        # Retailers
        micro_center = Retailer(
            name="Micro Center",
            website="https://www.microcenter.com",
            is_active=True,
        )
        best_buy = Retailer(
            name="Best Buy",
            website="https://www.bestbuy.com",
            is_active=True,
        )

        db.add_all([micro_center, best_buy])
        db.flush()

        # Products
        legion_pro_7i = Product(
            brand="Lenovo",
            model="Legion Pro 7i",
            sku="LEN-LEGION-PRO-7I-5090",
            gpu="RTX 5090",
            cpu="Core Ultra 9 275HX",
            ram_gb=32,
            storage_gb=2000,
            screen_size=16.0,
            resolution="2560x1600",
            panel="IPS",
            os="Windows 11 Pro",
            description="Lenovo Legion Pro 7i high-end gaming laptop",
        )

        scar_18 = Product(
            brand="ASUS",
            model="ROG Strix SCAR 18",
            sku="ASUS-SCAR-18-5090",
            gpu="RTX 5090",
            cpu="Core Ultra 9 275HX",
            ram_gb=64,
            storage_gb=2000,
            screen_size=18.0,
            resolution="2560x1600",
            panel="Mini-LED",
            os="Windows 11 Pro",
            description="ASUS ROG Strix SCAR 18 flagship gaming laptop",
        )

        db.add_all([legion_pro_7i, scar_18])
        db.flush()

        # Offers
        legion_offer = Offer(
            product_id=legion_pro_7i.id,
            retailer_id=micro_center.id,
            price=Decimal("3599.99"),
            currency="USD",
            url="https://www.microcenter.com/example-legion-pro-7i",
            in_stock=True,
        )

        scar_offer = Offer(
            product_id=scar_18.id,
            retailer_id=best_buy.id,
            price=Decimal("4299.99"),
            currency="USD",
            url="https://www.bestbuy.com/example-scar-18",
            in_stock=True,
        )

        db.add_all([legion_offer, scar_offer])
        db.flush()

        # Price history
        legion_history = PriceHistory(
            offer_id=legion_offer.id,
            price=Decimal("3599.99"),
        )
        scar_history = PriceHistory(
            offer_id=scar_offer.id,
            price=Decimal("4299.99"),
        )

        db.add_all([legion_history, scar_history])
        db.commit()

        print("Seed data inserted successfully.")

    except Exception as exc:
        db.rollback()
        raise exc
    finally:
        db.close()


if __name__ == "__main__":
    seed_database()
