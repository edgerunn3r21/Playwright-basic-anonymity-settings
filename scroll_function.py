def page_scroll(page, sleep=0.5):
    """Scrolls the page further based on the number and height of the search result elements."""

    # Get count of blocks
    block_count = page.evaluate(
        """() => {
                const el = document.querySelectorAll('<element>');
                return el ? el.length : 0;
            }"""
    )

    # Get block height
    block_height = page.evaluate(
        """() => {
                const el = document.querySelector('<element>');
                return el ? el.offsetHeight : 0;
            }"""
    )

    for _ in range(block_count):
        page.mouse.wheel(0, block_height)
        time.sleep(sleep)
