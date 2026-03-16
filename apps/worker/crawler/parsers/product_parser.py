import re


def extract_ram_gb(text: str) -> int | None:
    match = re.search(r"(\d+)\s*GB", text, re.IGNORECASE)
    return int(match.group(1)) if match else None


def extract_storage_gb(text: str) -> int | None:
    tb_match = re.search(r"(\d+)\s*TB", text, re.IGNORECASE)
    if tb_match:
        return int(tb_match.group(1)) * 1000

    gb_match = re.search(r"(\d+)\s*GB", text, re.IGNORECASE)
    return int(gb_match.group(1)) if gb_match else None


def extract_refresh_rate_hz(text: str) -> int | None:
    match = re.search(r"(\d+)\s*Hz", text, re.IGNORECASE)
    return int(match.group(1)) if match else None


def extract_screen_size(text: str) -> float | None:
    match = re.search(r'(\d+(?:\.\d+)?)["\']', text)
    return float(match.group(1)) if match else None
