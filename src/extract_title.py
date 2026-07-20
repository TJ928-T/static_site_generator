import re
from markdown_to_html import markdown_to_html_node



def extract_title(markdown):
    node = markdown_to_html_node(markdown)
    html = node.to_html()
    match = re.search(r"<h1>(.*?)</h1>", html)
    try:
        title = match.group(1)
        title = title.strip()
        return title
    except:
        raise Exception("There is no title in the html markdwon")

