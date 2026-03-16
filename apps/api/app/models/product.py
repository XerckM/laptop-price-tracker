from sqlalchemy import Float, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    brand: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    model: Mapped[str] = mapped_column(String(150), nullable=False, index=True)
    sku: Mapped[str | None] = mapped_column(String(100), nullable=True, unique=True)

    # CPU / GPU
    cpu: Mapped[str | None] = mapped_column(String(120), nullable=True, index=True)
    gpu: Mapped[str | None] = mapped_column(String(120), nullable=True, index=True)

    # Memory
    ram_gb: Mapped[int | None] = mapped_column(Integer, nullable=True)
    ram_type: Mapped[str | None] = mapped_column(String(50), nullable=True)
    ram_speed_mhz: Mapped[int | None] = mapped_column(Integer, nullable=True)

    # Storage
    storage_gb: Mapped[int | None] = mapped_column(Integer, nullable=True)
    storage_type: Mapped[str | None] = mapped_column(String(50), nullable=True)
    storage_interface: Mapped[str | None] = mapped_column(String(50), nullable=True)

    # Display
    screen_size: Mapped[float | None] = mapped_column(Float, nullable=True)
    resolution: Mapped[str | None] = mapped_column(String(50), nullable=True)
    panel_type: Mapped[str | None] = mapped_column(String(50), nullable=True)
    refresh_rate_hz: Mapped[int | None] = mapped_column(Integer, nullable=True)

    # Operating system
    os: Mapped[str | None] = mapped_column(String(100), nullable=True)

    # Extra
    description: Mapped[str | None] = mapped_column(Text, nullable=True)

    offers = relationship("Offer", back_populates="product", cascade="all, delete-orphan")
