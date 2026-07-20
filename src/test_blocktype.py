import unittest
from blocktype import block_to_block_type, BlockType, markdown_to_blocks



class TestBlockTypes(unittest.TestCase):
    def test_blocktype(self):
        header1 = "#### This is a header"
        header2 = "####### This is not a correct header"
        header3 = "This is not a correct ### header"
        code_block1 = "```\nThis is a correct code block```"
        code_block2 = "```\nThis is the start\nThis is the middle\nThis is the end of a code block\n```"
        code_block3 = "```This is not a correct code block```"
        quote1 = ">This is a quote"
        quote2 = "> This is a quote\n>With another quote"
        unordered_list1 = "- This is a list\n- This is a list\n- This is a list\n- This is a list"
        unordered_list2 = "- This is not a list\n- This is not a list\n-This is not a list"
        ordered_list1 = "1. One\n2. Two\n3. Three"
        ordered_list2 = "1. One\nTwo\n3. Three"
        ordered_list3 = "1. One\n3. Three\n4. Four"
        self.assertEqual(block_to_block_type(header1), BlockType.HEADING)
        self.assertEqual(block_to_block_type(header2), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(header3), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(code_block1), BlockType.CODE)
        self.assertEqual(block_to_block_type(code_block2), BlockType.CODE)
        self.assertEqual(block_to_block_type(code_block3), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(quote1), BlockType.QUOTE)
        self.assertEqual(block_to_block_type(quote2), BlockType.QUOTE)
        self.assertEqual(block_to_block_type(unordered_list1), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type(unordered_list2), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(ordered_list1), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type(ordered_list2), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(ordered_list3), BlockType.PARAGRAPH)


    def test_split_blocks(self):
        block = "# This is a heading \n\n   This is a paragraph of text. It has some **bold** and _italic_ words inside of it.\n\n- This is the first list item in " \
            "a list block\n- This is a list item\n- This is another list item"
        block2 = "# This is a heading\n\n       \n\nThis is a paragraph of text. It has some **bold** and _italic_ words inside of it.\n\n\n- This is the " \
            "first list item in a list block\n- This is a list item\n- This is another list item"
        block3 = ""
        self.assertEqual(markdown_to_blocks(block), ['# This is a heading', 'This is a paragraph of text. It has some **bold** and _italic_ words inside of it.',
                    '- This is the first list item in a list block\n- This is a list item\n- This is another list item'])
        self.assertEqual(markdown_to_blocks(block2), ['# This is a heading', 'This is a paragraph of text. It has some **bold** and _italic_ words inside of it.',
                    '- This is the first list item in a list block\n- This is a list item\n- This is another list item'])
        self.assertEqual(markdown_to_blocks(block3), [])