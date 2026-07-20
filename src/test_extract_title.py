import unittest
from extract_title import extract_title



class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        md = """
# This is a **header** ## text

This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here
"""
        md2 = """
### This is a **header** ## text

This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here
"""

        md3 = """
This is a **not** a header

# This is **bolded** header

This is paragraph with _italic_ text and `code` here
"""

        self.assertEqual(extract_title(md), "This is a <b>header</b> ## text")
        self.assertEqual(extract_title(md3), "This is <b>bolded</b> header")
        with self.assertRaises(Exception):
            extract_title(md2)