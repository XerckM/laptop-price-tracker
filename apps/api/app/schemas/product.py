from decimal import Decimal

from pydantic import BaseModel


class OfferResponse(BaseModel):
    id: int
    price: Decimal
    currency: str
    url: str
    in_stock: bool
    retailer_name: str

    class Config:
        from_attributes = True


class ProductBase(BaseModel):
    brand: str
    model: str

    cpu: str | None = None
    gpu: str | None = None

    ram_gb: int | None = None
    ram_type: str | None = None
    ram_speed_mhz: int | None = None

    storage_gb: int | None = None
    storage_type: str | None = None
    storage_interface: str | None = None

    screen_size: float | None = None
    resolution: str | None = None
    panel_type: str | None = None
    refresh_rate_hz: int | None = None

    os: str | None = None


class ProductResponse(ProductBase):
    id: int
    offers: list[OfferResponse] = []

    class Config:
        from_attributes = True
