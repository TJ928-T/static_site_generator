import re
from textnode import TextNode, TextType



def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
            new_nodes.append(old_node)
            continue
        if delimiter == "`":
            words = re.split(r'(`)', old_node.text)
            node_type = TextType.CODE
        if delimiter == "_":
            words = re.split(r'(_)', old_node.text)
            node_type = TextType.ITALIC
        if delimiter == "**":
            words = re.split(r'(\*\*)', old_node.text)
            node_type = TextType.BOLD
            
        words = list(filter(None, words))
        i = 0
        for x in range(len(words)):
            if words[x] == delimiter and i == 0:
                i += 1
                continue
            if words[x] == delimiter and i == 1:
                i -= 1
                continue
            if x == len(words) - 1 and i == 1:
                raise Exception("The delimiter does not have a matching pair")
            if i == 1:
                new_nodes.append(TextNode(words[x], node_type))
            if i != 1:
                new_nodes.append(TextNode(words[x], TextType.TEXT))

    return new_nodes

