from pydantic import BaseModel


class ProductBase(BaseModel):
    brand: str
    model: str
    gpu: str | None = None
    cpu: str | None = None
    ram_gb: int | None = None
    storage_gb: int | None = None


class ProductResponse(ProductBase):
    id: int

    class Config:
        from_attributes = True
