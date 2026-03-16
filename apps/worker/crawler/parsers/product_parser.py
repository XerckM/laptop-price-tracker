import html
import re
from decimal import Decimal
from typing import Any


KNOWN_BRANDS = [
    "Lenovo",
    "Acer",
    "HP",
    "MSI",
    "Dell",
    "ASUS",
    "Razer",
    "Gigabyte",
    "Alienware",
]


def clean_text(value: str | None) -> str | None:
    if not value:
        return None

    value = html.unescape(value)
    value = re.sub(r"\s+", " ", value).strip()
    return value or None


def extract_brand(title: str | None) -> str | None:
    title = clean_text(title)
    if not title:
        return None

    title_lower = title.lower()

    for brand in KNOWN_BRANDS:
        if title_lower.startswith(brand.lower() + " "):
            return brand

    # Infer common house-brand mappings from model names
    if title.startswith("ROG "):
        return "ASUS"
    if title.startswith("Predator ") or title.startswith("Nitro "):
        return "Acer"
    if title.startswith("OMEN ") or title.startswith("Victus "):
        return "HP"
    if title.startswith("Alienware "):
        return "Dell"

    return None


def extract_screen_size(title: str | None) -> float | None:
    title = clean_text(title)
    if not title:
        return None

    match = re.search(r"(\d+(?:\.\d+)?)\s*(?:\"|inch)", title, re.IGNORECASE)
    return float(match.group(1)) if match else None


def extract_model(title: str | None, brand: str | None) -> str | None:
    title = clean_text(title)
    if not title:
        return None

    model = title

    if brand and model.lower().startswith(brand.lower() + " "):
        model = model[len(brand):].strip()

    # Remove the trailing color after " - "
    model = re.sub(r"\s+-\s+.*$", "", model).strip()

    return model or None


def extract_current_price(price_text: str | None) -> Decimal | None:
    price_text = clean_text(price_text)
    if not price_text:
        return None

    # Prefer "Our price $X"
    match = re.search(r"Our price\s*\$([\d,]+(?:\.\d{2})?)", price_text, re.IGNORECASE)
    if match:
        return Decimal(match.group(1).replace(",", ""))

    # Fallback to last dollar amount on the string
    matches = re.findall(r"\$([\d,]+(?:\.\d{2})?)", price_text)
    if matches:
        return Decimal(matches[-1].replace(",", ""))

    return None


def normalize_microcenter_product(raw: dict[str, Any]) -> dict[str, Any]:
    title = clean_text(raw.get("title"))
    price_text = clean_text(raw.get("price_text"))
    url = clean_text(raw.get("url"))

    brand = extract_brand(title)
    model = extract_model(title, brand)
    screen_size = extract_screen_size(title)
    current_price = extract_current_price(price_text)

    return {
        "retailer_name": "Micro Center",
        "retailer_website": "https://www.microcenter.com",
        "brand": brand,
        "model": model,
        "sku": None,
        "cpu": None,
        "gpu": None,
        "ram_gb": None,
        "ram_type": None,
        "ram_speed_mhz": None,
        "storage_gb": None,
        "storage_type": None,
        "storage_interface": None,
        "screen_size": screen_size,
        "resolution": None,
        "panel_type": None,
        "refresh_rate_hz": None,
        "os": None,
        "description": title,
        "price": current_price,
        "currency": "USD",
        "url": url,
        "in_stock": True,
        "raw_title": title,
        "raw_price_text": price_text,
    }
