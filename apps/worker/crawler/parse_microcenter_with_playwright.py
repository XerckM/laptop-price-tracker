import asyncio
from pprint import pprint
from urllib.parse import urljoin

from playwright.async_api import TimeoutError as PlaywrightTimeoutError
from playwright.async_api import async_playwright


URL = "https://www.microcenter.com/search/search_results.aspx?fq=category:Laptops%2FNotebooks|618,Subcategory:Gaming+Laptops&rd=1"
BASE_URL = "https://www.microcenter.com"


async def click_if_visible(page, selector: str, label: str) -> None:
    try:
        locator = page.locator(selector).first
        if await locator.is_visible(timeout=3000):
            await locator.click()
            await page.wait_for_timeout(1500)
            print(f"Clicked: {label}")
    except Exception:
        pass


async def main() -> None:
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)

        context = await browser.new_context(
            user_agent=(
                "Mozilla/5.0 (X11; Linux x86_64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/123.0.0.0 Safari/537.36"
            ),
            viewport={"width": 1440, "height": 900},
            locale="en-US",
        )

        page = await context.new_page()
        await page.goto(URL, wait_until="domcontentloaded", timeout=60000)
        await page.wait_for_timeout(4000)

        print(f"Final URL: {page.url}")
        print(f"Page title: {await page.title()}")

        # Handle common modals/popups
        await click_if_visible(page, 'button:has-text("Allow All")', "Allow All cookies")
        await click_if_visible(page, 'button:has-text("Confirm My Choices")', "Confirm My Choices")
        await click_if_visible(page, 'button:has-text("Close Your Store Modal")', "Close store modal")
        await click_if_visible(page, 'button[aria-label="Close"]', "Generic close button")

        await page.wait_for_timeout(3000)

        # Debug counts
        product_count = await page.locator("li.product_wrapper").count()
        print(f"li.product_wrapper count: {product_count}")

        if product_count == 0:
            h2_texts = await page.locator("h2").all_text_contents()
            print("\nFirst 15 <h2> texts:")
            for text in h2_texts[:15]:
                cleaned = text.strip()
                if cleaned:
                    print("-", cleaned)

        products = await page.evaluate(
            """
            () => {
                const results = [];
                const cards = Array.from(document.querySelectorAll("li.product_wrapper"));

                for (const card of cards) {
                    const link =
                        card.querySelector("a.productClickItemV2.productViewItem") ||
                        card.querySelector("a.product-item__link.productClickItemV2") ||
                        card.querySelector("a.product-item__link") ||
                        card.querySelector("h2 a") ||
                        card.querySelector("a[href*='/product/']");

                    const title =
                        link?.getAttribute("data-name")?.trim() ||
                        link?.textContent?.trim() ||
                        null;

                    const href = link?.getAttribute("href") || null;

                    const priceEl =
                        card.querySelector(".product-item__price .text-blue") ||
                        card.querySelector(".product-item__price .font-size-2") ||
                        card.querySelector(".product-item__price") ||
                        card.querySelector(".price");

                    const priceText = priceEl?.textContent?.trim() || null;

                    results.push({
                        title,
                        href,
                        price_text: priceText,
                    });
                }

                return results;
            }
            """
        )

        print(f"\nFound {len(products)} products")

        for index, product in enumerate(products, start=1):
            normalized = {
                "title": product["title"],
                "url": urljoin(BASE_URL, product["href"]) if product["href"] else None,
                "price_text": product["price_text"],
            }

            print(f"\\nProduct #{index}")
            pprint(normalized)

        await context.close()
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
