from splitblocks import markdown_to_blocks, block_to_block_type, markdown_to_html
from parentnode import ParentNode
from textnode import TextNode
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




test = "###### "
test2 = "###### ###How now brown cow!!####"
test3 = "####### hiya"
test5 = "#"
test6 = "# "
test7 = "# #Hello##"
test8 = "``` Code Block ```"
test9 = "```Code Block```"
test10 = "``C`ode```"
test11 = "`Code`"
test12 = ">Quoteerino>>>>"
test13 = ">This is the first list item in a list block\n>This is a list item\n>* This is another list item'"
test14 = ">This is the first list item in a list block\nThis is a list item\n>* This is another list item'"
test15 = "This is the first list item in a list block\n>This is a list item\n>* This is another list item'"
test16 = "* This is the first list item in a list block\n>This is a list item\n* This is another list item'"
test17 = "* This is the first list item in a list block\n* This is a list item\n* This is another list item'"
test18 = "- This is the first list item in a list block\n- This is a list item\n- This is another list item'"
test19 = "- This is the first list item in a list block\n* This is a list item\n- This is another list item'"
test20 = "- This is the first list item in a list block\nThis is a list item\n- This is another list item'"
test21 = "1. This is the first list item in a list block\n2. This is a list item\n3. This is another list item'"
test22 = "This is the first list item in a list block\n2. This is a list item\n3. This is another list item'"
test23 = "25555555555. This is the first list item in a list block\n2. This is a list item\n3000000000000. This is another list item'"
test24 = "25555555555. This is the first list item in a list block\n20.This is a list item\n3000000000000. This is another list item'"
test25 = "25555555555. This is the first list item in a list block\n20. This is a list item\n3000000000000. This is another list item'"
test26 = "# Heading2! 25555555555. This is the first list item in a list block\n20. This is a list item\n3000000000000."
test27 = "#Heading2!"
test28 = "nwowowowoow"



class TestBlockToBlockType(unittest.TestCase):

    def test_all(self):
        test_cases = [
            (test, "heading"),
            (test2, "heading"),
            (test3, "paragraph"),
            (test5, "paragraph"),
            (test6, "heading"),
            (test7, "heading"),
            (test8, "code"),
            (test9, "code"),
            (test10, "paragraph"),
            (test11, "paragraph"),
            (test12, "quote"),
            (test13, "quote"),
            (test14, "paragraph"),
            (test15, "paragraph"),
            (test16, "paragraph"),
            (test17, "unordered list"),
            (test18, "unordered list"),
            (test19, "unordered list"),
            (test20, "paragraph"),
            (test21, "ordered list"),
            (test22, "paragraph"),
            (test23, "ordered list"),
            (test24, "paragraph"),
            (test25, "ordered list"),
            (test26, "heading"),
            (test27, "paragraph"),
            (test28, "paragraph")
        ]
        for inp, expected in test_cases:
            with self.subTest(inp=inp, expected=expected):
                result = block_to_block_type(inp)
                self.assertEqual(result, expected)




textnodes_list = [
    TextNode("This is a heading\nThis is a paragraph of text. It has some ", "text", None), 
    TextNode("bold", "bold", None), 
    TextNode(" and ", "text", None), 
    TextNode("italic", "italic", None), 
    TextNode(" words inside of it.\n", "text", None), 
    TextNode(" This is the first list item in a list block\n", "italic", None), 
    TextNode(" This is a list item\n", "text", None), 
    TextNode(" This is another list item\n## Heading 2\n", "italic", None), 
    TextNode(" This is the first list item in a list block\n", "text", None), 
    TextNode(" This is a list item\n", "italic", None), 
    TextNode(" This is another list item\n# Wow, just wow.", "text", None)
                  ]
#Expected Results for markdown to html
markdowntohtmlexpectedresult1 = ParentNode("div", [ParentNode("h1", list(map(lambda x: x.text_node_to_html_node(), textnodes_list)), None)], None).to_html()
markdowntohtmlexpectedresult2 = "<div><h1>This is a heading</h1><p>This is a paragraph of text. It has some <b>bold</b> and <i>italic</i> words inside of it.</p><ul><li>This is the first list item in a list block</li><li>This is a list item</li><li>This is another list item</li></ul><h2>Heading 2</h2><ul><li>This is the first list item in a list block</li><li>This is a list item</li><li>This is another list item</li></ul><h1>Wow, just wow.</h1></div>"
markdowntohtmlexpectedresult3 = "<div><h1>This is a heading</h1><p>This is a paragraph of text. It has some <b>bold</b> and <i>italic</i> words inside of it.</p><ul><li>This is the first list item in a list block</li><li>This is a list item</li><li>This is another list item</li></ul><h2>Heading 2</h2><ul><li>This is the first list item in a list block</li><li>This is a list item</li><li>This is another list item</li></ul><h1>Wow, just wow.</h1></div>"
markdowntohtmlexpectedresult4 = "<div><h1>This is a heading</h1><p>This is a paragraph of text. It has some <b>bold</b> and <i>italic</i> words inside of it.</p><ul><li>This is the first list item in a list block</li><li>This is a list item</li><li>This is another list item</li></ul><h2>Heading 2</h2><ul><li>This is the first list item in a list block</li><li>This is a list item</li></ul><ul><li>This is another list item</li></ul><h1>Wow, just wow.</h1></div>"


class TestMarkdown_to_html(unittest.TestCase):

    def test_all(self):
        test_cases = [
            (markdown_one_block, markdowntohtmlexpectedresult1),
             (markdown_expected, markdowntohtmlexpectedresult2),
             (markdown_multiple_sets_of_blank_rows_leading_and_trailing, markdowntohtmlexpectedresult3),
             (markdown_text_crazy_mix, markdowntohtmlexpectedresult4),
        ]
        count = 0
        for inp, expected in test_cases:
            with self.subTest(inp=inp, expected=expected):
                count += 1
                result = markdown_to_html(inp).to_html()
                self.assertEqual(result, expected)
                print(f"{count}: {result}")