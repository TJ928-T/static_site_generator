import unittest
from extract_links_images import extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

class TestLinksImages(unittest.TestCase):
    def test_extract_markdown_images(self):
        link = extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")
        link2 = extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan]")
        link3 = extract_markdown_images("This does not contain a pair of alt text and image url")
        self.assertEqual(link, [('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')])
        self.assertEqual(link2, [('rick roll', 'https://i.imgur.com/aKaOqIh.gif')])
        self.assertEqual(link3, [])


    def test_extract_markdown_links(self):
        link = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
        link2 = extract_markdown_links("This is text with a link [to boot dev] and [to youtube](https://www.youtube.com/@bootdotdev)")
        link3 = extract_markdown_links("This does not contain any anchor text or urls")
        self.assertEqual(link, [('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')])
        self.assertEqual(link2, [('to youtube', 'https://www.youtube.com/@bootdotdev')])
        self.assertEqual(link3, [])

    def test_split_nodes_images(self):
        link = split_nodes_image([TextNode(
    "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
    TextType.TEXT,
     )])
        link2 = split_nodes_image([TextNode(
     "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image]",
    TextType.TEXT,
    )])
        link3 = split_nodes_image([TextNode(
    "This text does not contain any images with url links",
    TextType.TEXT,
    )])
        link4 = split_nodes_image([TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT),
                                   TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image]", TextType.TEXT),
                                   TextNode("This text does not contain any images with url links", TextType.TEXT)])
        self.assertEqual(link, [TextNode('This is text with an ', TextType.TEXT), TextNode('image', TextType.IMAGE, 'https://i.imgur.com/zjjcJKZ.png'),
                            TextNode(' and another ', TextType.TEXT), TextNode('second image', TextType.IMAGE, 'https://i.imgur.com/3elNhQu.png')])
        self.assertEqual(link2, [TextNode('This is text with an ', TextType.TEXT), TextNode('image', TextType.IMAGE, 'https://i.imgur.com/zjjcJKZ.png'),
                            TextNode(' and another ![second image]', TextType.TEXT)])
        self.assertEqual(link3, [TextNode("This text does not contain any images with url links", TextType.TEXT)])
        self.assertEqual(link4, [TextNode('This is text with an ', TextType.TEXT),
                            TextNode('image', TextType.IMAGE, 'https://i.imgur.com/zjjcJKZ.png'), TextNode(' and another ', TextType.TEXT),
                            TextNode('second image', TextType.IMAGE, 'https://i.imgur.com/3elNhQu.png'), TextNode('This is text with an ', TextType.TEXT),
                            TextNode('image', TextType.IMAGE, 'https://i.imgur.com/zjjcJKZ.png'), TextNode(' and another ![second image]', TextType.TEXT),
                            TextNode("This text does not contain any images with url links", TextType.TEXT)])


    def test_split_nodes_links(self):
        link = split_nodes_link([TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.TEXT,
    )])
        link2 = split_nodes_link([TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube]",
    TextType.TEXT,
    )])
        link3 = split_nodes_link([TextNode(
    "This text does not contain any link text with url links",
    TextType.TEXT,
    )])
        link4 = split_nodes_link([TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT),
    TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube]", TextType.TEXT),
    ])
        self.assertEqual(link, [TextNode('This is text with a link ', TextType.TEXT), TextNode('to boot dev', TextType.LINK, 'https://www.boot.dev'), TextNode(' and ', TextType.TEXT), TextNode('to youtube', TextType.LINK, 'https://www.youtube.com/@bootdotdev')])
        self.assertEqual(link2, [TextNode('This is text with a link ', TextType.TEXT), TextNode('to boot dev', TextType.LINK, 'https://www.boot.dev'), TextNode(' and [to youtube]', TextType.TEXT)])
        self.assertEqual(link3, [TextNode("This text does not contain any link text with url links", TextType.TEXT)])
        self.assertEqual(link4, [TextNode('This is text with a link ', TextType.TEXT), TextNode('to boot dev', TextType.LINK, 'https://www.boot.dev'),
                                TextNode(' and ', TextType.TEXT), TextNode('to youtube', TextType.LINK, 'https://www.youtube.com/@bootdotdev'),
                                TextNode('This is text with a link ', TextType.TEXT), TextNode('to boot dev', TextType.LINK, 'https://www.boot.dev'),
                                TextNode(' and [to youtube]', TextType.TEXT)])




if __name__ == "__main__":
    unittest.main()
        