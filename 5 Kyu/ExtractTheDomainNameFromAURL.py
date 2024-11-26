import re

def domain_name(url):
    domain = re.search(r"(?:https?://)?(?:www\.)?([^./]+)", url).group(1)
    return domain