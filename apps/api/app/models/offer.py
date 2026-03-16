from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Index, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class Offer(Base):
    __tablename__ = "offers"
    __table_args__ = (
        Index("ix_offers_product_price", "product_id", "price"),
        Index("ix_offers_retailer_id", "retailer_id"),
        Index("ix_offers_in_stock", "in_stock"),
    )

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), nullable=False, index=True)
    retailer_id: Mapped[int] = mapped_column(ForeignKey("retailers.id"), nullable=False, index=True)

    price: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False, index=True)
    currency: Mapped[str] = mapped_column(String(10), default="USD", nullable=False)
    url: Mapped[str] = mapped_column(String(500), nullable=False)
    in_stock: Mapped[bool] = mapped_column(default=True, nullable=False)

    last_seen_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    product = relationship("Product", back_populates="offers")
    retailer = relationship("Retailer", back_populates="offers")
    price_history = relationship("PriceHistory", back_populates="offer", cascade="all, delete-orphan")
