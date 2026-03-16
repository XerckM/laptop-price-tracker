import asyncio
from pathlib import Path

from playwright.async_api import async_playwright


URL = "https://www.microcenter.com/search/search_results.aspx?N=4294967288+4294807523"


async def main() -> None:
    output_path = Path("microcenter_debug.html")

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
        )

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
        await page.wait_for_timeout(5000)

        print(f"Final URL: {page.url}")
        print(f"Page title: {await page.title()}")

        html = await page.content()
        output_path.write_text(html, encoding="utf-8")

        print(f"Saved HTML to {output_path.resolve()}")

        await context.close()
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
