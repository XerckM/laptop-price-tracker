from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.product import OfferResponse, ProductResponse
from app.services.product_service import get_product_by_id, get_products

router = APIRouter(prefix="/products", tags=["products"])


def serialize_product(product) -> ProductResponse:
    return ProductResponse(
        id=product.id,
        brand=product.brand,
        model=product.model,
        cpu=product.cpu,
        gpu=product.gpu,
        ram_gb=product.ram_gb,
        ram_type=product.ram_type,
        ram_speed_mhz=product.ram_speed_mhz,
        storage_gb=product.storage_gb,
        storage_type=product.storage_type,
        storage_interface=product.storage_interface,
        screen_size=product.screen_size,
        resolution=product.resolution,
        panel_type=product.panel_type,
        refresh_rate_hz=product.refresh_rate_hz,
        os=product.os,
        offers=[
            OfferResponse(
                id=offer.id,
                price=offer.price,
                currency=offer.currency,
                url=offer.url,
                in_stock=offer.in_stock,
                retailer_name=offer.retailer.name if offer.retailer else "Unknown",
            )
            for offer in product.offers
        ],
    )


@router.get("", response_model=list[ProductResponse])
def list_products(db: Session = Depends(get_db)):
    products = get_products(db)
    return [serialize_product(product) for product in products]


@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = get_product_by_id(db, product_id)

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return serialize_product(product)
