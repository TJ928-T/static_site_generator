import unittest
from text_to_textnodes import text_to_textnode
from textnode import TextNode, TextType


class TestTextToNodes(unittest.TestCase):
    def test_text_to_nodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a " \
            "[link](https://boot.dev)"
        text2 = "This is **text** with an _italic_ word and a **bold block** and an [link](https://i.imgur.com/fJRm4Vk.jpeg) and another " \
            "[link](https://boot.dev)"
        text3 = "This is just a plain text sentence that contains no other TextTypes"
        self.assertEqual(text_to_textnode(text), [
    TextNode("This is ", TextType.TEXT),
    TextNode("text", TextType.BOLD),
    TextNode(" with an ", TextType.TEXT),
    TextNode("italic", TextType.ITALIC),
    TextNode(" word and a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" and an ", TextType.TEXT),
    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
    TextNode(" and a ", TextType.TEXT),
    TextNode("link", TextType.LINK, "https://boot.dev"),
    ])
        self.assertEqual(text_to_textnode(text2), [
    TextNode("This is ", TextType.TEXT),
    TextNode("text", TextType.BOLD),
    TextNode(" with an ", TextType.TEXT),
    TextNode("italic", TextType.ITALIC),
    TextNode(" word and a ", TextType.TEXT),
    TextNode("bold block", TextType.BOLD),
    TextNode(" and an ", TextType.TEXT),
    TextNode("link", TextType.LINK, "https://i.imgur.com/fJRm4Vk.jpeg"),
    TextNode(" and another ", TextType.TEXT),
    TextNode("link", TextType.LINK, "https://boot.dev"), 
        ])
        self.assertEqual(text_to_textnode(text3), [
    TextNode("This is just a plain text sentence that contains no other TextTypes", TextType.TEXT)
        ])