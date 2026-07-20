import re
from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def block_to_block_type(markdown: str) -> BlockType:
    if (re.match(r"(?:^#{1,6}\s)", markdown) is not None) == True:
        return BlockType.HEADING
    if (re.fullmatch(r"```\n(?:^.*(?:\n|```$))+", markdown, re.MULTILINE) is not None) == True:
        return BlockType.CODE
    if (re.fullmatch(r"(?:^>\s{0,1}\S.*(?:\n|$))+", markdown, re.MULTILINE) is not None) == True:
        return BlockType.QUOTE
    if (re.fullmatch(r"(?:^-\s\S.*(?:\n|$))+", markdown, re.MULTILINE) is not None) == True:
        return BlockType.UNORDERED_LIST
    if (re.fullmatch(r"(?:^\d+\.\s\S.*(?:\n|$))+", markdown, re.MULTILINE) is not None) == True:
        order_list = markdown.split("\n")
        i = 1
        for x in order_list:
            if (x[0] == str(i)) == False:
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH


def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split("\n\n")
    clean_blocks = []
    for block in blocks:
        res = block.strip()
        if res == "":
            continue
        clean_blocks.append(res)
    return clean_blocks