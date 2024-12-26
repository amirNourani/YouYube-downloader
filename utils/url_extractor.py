import re
from typing import Optional


def extract_urls(text: str) -> Optional[str]:
    """Extract all URLs from the given text."""
    # Regular expression pattern for URLs
    url_pattern = r"https?://[^\s]+"
    urls = re.findall(url_pattern, text)
    return urls[0] if urls else None
