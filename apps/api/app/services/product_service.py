from sqlalchemy.orm import Session, joinedload

from app.models.offer import Offer
from app.models.product import Product


def get_products(db: Session):
    return (
        db.query(Product)
        .options(
            joinedload(Product.offers).joinedload(Offer.retailer)
        )
        .all()
    )


def get_product_by_id(db: Session, product_id: int):
    return (
        db.query(Product)
        .options(
            joinedload(Product.offers).joinedload(Offer.retailer)
        )
        .filter(Product.id == product_id)
        .first()
    )
