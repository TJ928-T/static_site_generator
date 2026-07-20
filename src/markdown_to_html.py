import re
from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode, ParentNode
from blocktype import BlockType, block_to_block_type, markdown_to_blocks
from text_to_textnodes import text_to_textnode




def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    blocks_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        block = clean_block_text(block, block_type)
        if block_type is not BlockType.CODE:
            leafnodes = text_to_leafnodes(block)
            text = leafnodes_to_html(leafnodes)
        else:
            code = TextNode(block, TextType.CODE)
            child = text_node_to_html_node(code)
            text = child.to_html()
        block_node = block_type_to_html(text, block_type)
        blocks_nodes.append(block_node)
    parent = ParentNode("div", blocks_nodes)
    return parent


def text_to_leafnodes(text: str) -> list[LeafNode]:
    textnode_list = text_to_textnode(text)
    children_nodes = []
    for textnode in textnode_list:
        child_node = text_node_to_html_node(textnode)
        children_nodes.append(child_node)
    return children_nodes

def block_type_to_html(text: str, text_type: BlockType) -> LeafNode:
    if text_type is BlockType.PARAGRAPH:
        return LeafNode("p", text)
    if text_type is BlockType.HEADING:
        i = re.findall(r"(?:^#{1,6})", text)
        text = text.split(i[0], 1)
        text = text[1].strip()
        return LeafNode(f"h{len(i[0])}", text)
    if text_type is BlockType.CODE:
        return LeafNode("pre", text)
    if text_type is BlockType.QUOTE:
        return LeafNode("blockquote", text)
    if text_type is BlockType.UNORDERED_LIST:
        return LeafNode("ul", text)
    if text_type is BlockType.ORDERED_LIST:
        return LeafNode("ol", text)

def leafnodes_to_html(leafnodes: list[LeafNode]) -> str:
    leafnodes_text = ""
    for node in leafnodes:
        leafnodes_text += node.to_html()
        leafnodes_text = leafnodes_text.replace("\n", " ")
    return leafnodes_text

def clean_block_text(block: str, block_type: BlockType) -> str:
    if block_type is BlockType.CODE:
        block = block.strip("```")
        block = block.strip()
    if block_type is BlockType.QUOTE:
        blocks = block.split(">")
        split_block = []
        for text in blocks:
                if text != "":
                    split_block.append(text.strip())
        block = " ".join(split_block)
    if block_type is BlockType.UNORDERED_LIST or block_type is BlockType.ORDERED_LIST:
        block = add_html_to_list_items(block, block_type)
    else:
        block = " ".join(block.split())
    return block

def add_html_to_list_items(text: str, blocktype: BlockType) -> str:
    lists = text.split("\n")
    html_tag_list = []
    for list in lists:
        if blocktype is BlockType.UNORDERED_LIST:
            list = f"<li>{list[1:].strip()}</li>"
        else:
            list = f"<li>{list[2:].strip()}</li>"
        html_tag_list.append(list)
    list_str = "".join(html_tag_list)
    return list_str
