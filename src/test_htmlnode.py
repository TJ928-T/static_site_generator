import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode



class TestTextNode(unittest.TestCase):
    def test_html_props(self):
        node = HTMLNode("p", "This is a test paragraph",props={"summary":"test"})
        node2 = HTMLNode("h1", "This is the top header", "h2", )
        node3 = HTMLNode("a", props={"href": "https://www.google.com", "target": "_blank",})
        self.assertEqual(node.props_to_html(), " summary=test")
        self.assertEqual(node2.props_to_html(), "")
        self.assertEqual(node3.props_to_html(), " href=https://www.google.com target=_blank")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        node2 = LeafNode("p", "This is a test paragraph",props={"summary":"test"})
        node3 = LeafNode(None, "This is a test with no tag")
        node4 = LeafNode("p", None)
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        self.assertEqual(node2.to_html(), "<p summary=test>This is a test paragraph</p>")
        self.assertEqual(node3.to_html(), "This is a test with no tag")
        self.assertRaises(ValueError, node4.to_html)

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        child_node2 = LeafNode("p", "second child")
        parent_node = ParentNode("div", [child_node])
        no_tag_parent = ParentNode(None, [child_node])
        childless_parent = ParentNode("div", None)
        multiple_children = ParentNode("div", [child_node, child_node2])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
        self.assertRaises(ValueError, no_tag_parent.to_html)
        self.assertRaises(ValueError, childless_parent.to_html)
        self.assertEqual(multiple_children.to_html(), "<div><span>child</span><p>second child</p></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        child_node2 = LeafNode("p", "second child")
        parent_node = ParentNode("div", [child_node])
        parent_node2 = ParentNode("div", [child_node, child_node2])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
        self.assertEqual(parent_node2.to_html(), "<div><span><b>grandchild</b></span><p>second child</p></div>")



if __name__ == "__main__":
    unittest.main()