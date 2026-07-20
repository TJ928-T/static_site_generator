import unittest
from textnode import TextNode, TextType, text_node_to_html_node



class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.ITALIC)
        node4 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        node5 = TextNode("This is a test", TextType.BOLD)
        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node, node4)
        self.assertNotEqual(node, node5)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

        node2 = TextNode("This is a bold node", TextType.BOLD)
        html_node2 = text_node_to_html_node(node2)
        self.assertEqual(html_node2.tag, "b")
        self.assertEqual(html_node2.value, "This is a bold node")

        node3 = TextNode("This is an italic node", TextType.ITALIC)
        html_node3 = text_node_to_html_node(node3)
        self.assertEqual(html_node3.tag, "i")
        self.assertEqual(html_node3.value, "This is an italic node")

        node4 = TextNode("This is a code node", TextType.CODE)
        html_node4 = text_node_to_html_node(node4)
        self.assertEqual(html_node4.tag, "code")
        self.assertEqual(html_node4.value, "This is a code node")

        node5 = TextNode("This is a link node", TextType.LINK, "https://www.boot.dev")
        html_node5 = text_node_to_html_node(node5)
        self.assertEqual(html_node5.tag, "a")
        self.assertEqual(html_node5.value, "This is a link node")
        self.assertEqual(html_node5.props, "href: https://www.boot.dev")

        node6 = TextNode("This is an image node", TextType.IMAGE, "https://www.boot.dev")
        html_node6 = text_node_to_html_node(node6)
        self.assertEqual(html_node6.tag, "img")
        self.assertEqual(html_node6.value, None)
        self.assertEqual(html_node6.props, "src: https://www.boot.dev, alt: This is an image node")

        node7 = TextNode("This is an invalid node", TextType.NORMAL, "https://www.boot.dev")
        with self.assertRaises(Exception):
            text_node_to_html_node(node7)


if __name__ == "__main__":
    unittest.main()