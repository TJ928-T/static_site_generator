import re
from textnode import TextNode, TextType



def extract_markdown_images(text: str) -> list[tuple]:
    match = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    # if len(match) == 0:
    #     raise Exception("The text does not contain a pair of alt text and image url")
    return match
    

def extract_markdown_links(text: str) -> list[tuple]:
    match = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    # if len(match) == 0:
    #     raise Exception("The text does not contain a pair of anchor text and url")
    return match


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
            new_nodes.append(old_node)
            continue
        images = extract_markdown_images(old_node.text)
        text_image = []
        url_image = []
        for image in images:
            text_image.append(image[0])
            url_image.append(image[1])
        words = re.split(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", old_node.text)
        words = list(filter(None, words))
        for x in range(len(words)):
            if words[x] in text_image:
                new_nodes.append(TextNode(words[x], TextType.IMAGE, words[x + 1]))
                continue
            if words[x] in url_image:
                continue
            new_nodes.append(TextNode(words[x], TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
            new_nodes.append(old_node)
            continue
        links = extract_markdown_links(old_node.text)
        text_link = []
        url_link = []
        for link in links:
            text_link.append(link[0])
            url_link.append(link[1])
        words = re.split(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", old_node.text)
        words = list(filter(None, words))
        for x in range(len(words)):
            if words[x] in text_link:
                new_nodes.append(TextNode(words[x], TextType.LINK, words[x + 1]))
                continue
            if words[x] in url_link:
                continue
            new_nodes.append(TextNode(words[x], TextType.TEXT))
    return new_nodes

