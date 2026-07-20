from textnode import TextNode, TextType
from splitnode import split_nodes_delimiter
from extract_links_images import split_nodes_image, split_nodes_link



def text_to_textnode(text: str) -> list[TextNode]:
    node = TextNode(text, TextType.TEXT)
    nodes = split_nodes_image([node])
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "`")
    nodes = split_nodes_delimiter(nodes, "_")
    nodes = split_nodes_delimiter(nodes, "**")
    return nodes

