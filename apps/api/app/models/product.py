from sqlalchemy import Float, Index, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class Product(Base):
    __tablename__ = "products"
    __table_args__ = (
        Index("ix_products_brand_model", "brand", "model"),
        Index("ix_products_gpu", "gpu"),
        Index("ix_products_cpu", "cpu"),
        Index("ix_products_ram_gb", "ram_gb"),
        Index("ix_products_storage_gb", "storage_gb"),
        Index("ix_products_screen_size", "screen_size"),
        Index("ix_products_refresh_rate_hz", "refresh_rate_hz"),
        Index("ix_products_os", "os"),
    )

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    brand: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    model: Mapped[str] = mapped_column(String(150), nullable=False, index=True)
    sku: Mapped[str | None] = mapped_column(String(100), nullable=True, unique=True)

    cpu: Mapped[str | None] = mapped_column(String(120), nullable=True, index=True)
    gpu: Mapped[str | None] = mapped_column(String(120), nullable=True, index=True)

    ram_gb: Mapped[int | None] = mapped_column(Integer, nullable=True)
    ram_type: Mapped[str | None] = mapped_column(String(50), nullable=True)
    ram_speed_mhz: Mapped[int | None] = mapped_column(Integer, nullable=True)

    storage_gb: Mapped[int | None] = mapped_column(Integer, nullable=True)
    storage_type: Mapped[str | None] = mapped_column(String(50), nullable=True)
    storage_interface: Mapped[str | None] = mapped_column(String(50), nullable=True)

    screen_size: Mapped[float | None] = mapped_column(Float, nullable=True)
    resolution: Mapped[str | None] = mapped_column(String(50), nullable=True)
    panel_type: Mapped[str | None] = mapped_column(String(50), nullable=True)
    refresh_rate_hz: Mapped[int | None] = mapped_column(Integer, nullable=True)

    os: Mapped[str | None] = mapped_column(String(100), nullable=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)

    offers = relationship("Offer", back_populates="product", cascade="all, delete-orphan")
