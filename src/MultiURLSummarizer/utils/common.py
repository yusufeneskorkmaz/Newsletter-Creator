import re

def is_valid_url(url):
    """Check if the given string is a valid URL."""
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None

def clean_text(text):
    """Clean and format the text."""
    # Remove extra whitespace
    text = ' '.join(text.split())
    # Capitalize the first letter of each sentence
    text = '. '.join(s.capitalize() for s in text.split('. '))
    return text