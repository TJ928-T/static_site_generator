import unittest
from splitnode import split_nodes_delimiter
from textnode import TextNode, TextType



class TestSplitNode(unittest.TestCase):
    def test_split_node(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        node2 = TextNode("This is a **bold word**", TextType.TEXT)
        node3 = TextNode("_This is an_ italic sentence", TextType.TEXT)
        node4 = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        node5 = TextNode("This is a normal text", TextType.TEXT)
        node6 = TextNode("This has **double** the **bold** words", TextType.TEXT)
        node7 = TextNode("This is text with a `code block word", TextType.TEXT)
        self.assertEqual(split_nodes_delimiter([node], "`"), [TextNode('This is text with a ', TextType.TEXT), TextNode('code block', TextType.CODE), TextNode(' word', TextType.TEXT)])
        self.assertEqual(split_nodes_delimiter([node2, node6], "**"), [TextNode('This is a ', TextType.TEXT), TextNode('bold word', TextType.BOLD), TextNode('This has ', TextType.TEXT), TextNode('double', TextType.BOLD), TextNode(' the ', TextType.TEXT), TextNode('bold', TextType.BOLD), TextNode(' words', TextType.TEXT)])
        self.assertEqual(split_nodes_delimiter([node3], "_"), [TextNode('This is an', TextType.ITALIC), TextNode(' italic sentence', TextType.TEXT)])
        self.assertEqual(split_nodes_delimiter([node4], "`"), [TextNode('This is an image', TextType.IMAGE, 'https://www.boot.dev')])
        self.assertEqual(split_nodes_delimiter([node5], "`"), [TextNode('This is a normal text', TextType.TEXT)])
        with self.assertRaises(Exception):
            split_nodes_delimiter([node7], "`")




if __name__ == "__main__":
    unittest.main()