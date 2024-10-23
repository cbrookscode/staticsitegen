from splitblocks import markdown_to_blocks
import unittest

markdown_empty = ""

markdown_one_block = """
# This is a heading
This is a paragraph of text. It has some **bold** and *italic* words inside of it.
* This is the first list item in a list block
* This is a list item
* This is another list item
## Heading 2
* This is the first list item in a list block
* This is a list item
* This is another list item
# Wow, just wow.
"""

markdown_expected = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item

## Heading 2

* This is the first list item in a list block
* This is a list item
* This is another list item

# Wow, just wow.
"""

markdown_multiple_sets_of_blank_rows_leading_and_trailing = """



# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.




* This is the first list item in a list block
* This is a list item
* This is another list item




## Heading 2



* This is the first list item in a list block
* This is a list item
* This is another list item



# Wow, just wow.

"""



markdown_text_crazy_mix = """



# This is a heading




This is a paragraph of text. It has some **bold** and *italic* words inside of it.


* This is the first list item in a list block
* This is a list item
* This is another list item




## Heading 2

* This is the first list item in a list block
* This is a list item



* This is another list item



# Wow, just wow.
"""

class TestMarkdownToBlocks(unittest.TestCase):
    def test_empty_markdown_text(self):
        with self.assertRaises(Exception) as context:
            markdown_to_blocks(markdown_empty)
        self.assertEqual(str(context.exception), "No Markdown Text Provided")
    
    def test_expected_markdown(self):
        result = markdown_to_blocks(markdown_expected)
        expected = ['# This is a heading', 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', '* This is the first list item in a list block\n* This is a list item\n* This is another list item', '## Heading 2', 
                    '* This is the first list item in a list block\n* This is a list item\n* This is another list item', '# Wow, just wow.'
        ]
        self.assertEqual(result, expected, f"Expected {expected} but got {result}")

    def test_multiple_sets_of_blank_rows_leading_and_trailing(self):
        result = markdown_to_blocks(markdown_multiple_sets_of_blank_rows_leading_and_trailing)
        expected = ['# This is a heading', 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', '* This is the first list item in a list block\n* This is a list item\n* This is another list item', '## Heading 2', 
         '* This is the first list item in a list block\n* This is a list item\n* This is another list item', '# Wow, just wow.'
        ]
        self.assertEqual(result, expected, f"Expected {expected} but got {result}")

    def test_crazy_mix_yo(self):
        result = markdown_to_blocks(markdown_text_crazy_mix)
        expected = [
            '# This is a heading', 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', '* This is the first list item in a list block\n* This is a list item\n* This is another list item', '## Heading 2', 
            '* This is the first list item in a list block\n* This is a list item', '* This is another list item', '# Wow, just wow.'
            ]
        self.assertEqual(result, expected, f"Expected {expected} but got {result}")

    def test_one_markdown_block(self):
        result = markdown_to_blocks(markdown_one_block)
        expected = ['# This is a heading\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n* This is the first list item in a list block\n* This is a list item\n* This is another list item\n## Heading 2\n* This is the first list item in a list block\n* This is a list item\n* This is another list item\n# Wow, just wow.']
        self.assertEqual(result, expected, f"Expected {expected} but got {result}")