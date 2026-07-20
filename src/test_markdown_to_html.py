import unittest
from markdown_to_html import markdown_to_html_node



class TestLinksImages(unittest.TestCase):
    def test_markdwon_to_html(self):
        md_paragraph = markdown_to_html_node("""
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

 """)
        md_heading = markdown_to_html_node("""
#### This is a **header** ## text
""")
        md_code = markdown_to_html_node("""
```
This is text that _should_ remain
the **same** even with inline stuff
```
""")
        md_quote = markdown_to_html_node("""
> This is a _quote_ block
>That **contains** multiple lines
""")
        md_unordered = markdown_to_html_node("""
- This is **item one**
- This is the _second_ item
- This is the `third` item
""")
        md_ordered = markdown_to_html_node("""
1. This is **item one**
2. This is the _second_ item
3. This is the `third` item
""")
        self.assertEqual(md_paragraph.to_html(), "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>")
        self.assertEqual(md_heading.to_html(), "<div><h4>#### This is a <b>header</b> ## text</h4></div>")
        self.assertEqual(md_code.to_html(), "<div><pre><code>This is text that _should_ remain the **same** even with inline stuff</code></pre></div>")
        self.assertEqual(md_quote.to_html(), "<div><blockquote>This is a <i>quote</i> block That <b>contains</b> multiple lines</blockquote></div>")
        self.assertEqual(md_unordered.to_html(), "<div><ul><li>This is <b>item one</b></li><li>This is the <i>second</i> item</li><li>This is the <code>third</code> item</li></ul></div>")
        self.assertEqual(md_ordered.to_html(), "<div><ol><li>This is <b>item one</b></li><li>This is the <i>second</i> item</li><li>This is the <code>third</code> item</li></ol></div>")