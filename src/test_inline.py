from textnode import TextNode
from inline import split_nodes_delimeter

import unittest

# split_nodes_delimeter(old_nodes, delimiter, text_type)

node = [TextNode("This is text with a `code block` word", "text"), TextNode("testing", "italic")]
node2 = [TextNode("This is text `with` a word", "text"), TextNode("testing", "text"), TextNode("how *now* brown cow", "italic")]
node3 = [TextNode("This is text **with** a word", "text"), TextNode("testing", "text"), TextNode("how *now* brown cow", "italic")]

class TestInlineFunctions(unittest.TestCase):
    def test_no_delimeter(self):
        with self.assertRaises(Exception) as context:
            split_nodes_delimeter(node, "", "code")
        self.assertEqual(str(context.exception), "Requires delimeter to be entered")

    def test_empty_textnode(self):
        with self.assertRaises(TypeError) as context:
            split_nodes_delimeter()

    def test_empty_old_nodes(self):
        with self.assertRaises(Exception) as context:
            split_nodes_delimeter([], "`", "code")
        self.assertEqual(str(context.exception), "Cannot provide an empty node list")

    def test_empty_text_type(self):
        with self.assertRaises(Exception) as context:
            split_nodes_delimeter(node, "`", "")
        self.assertEqual(str(context.exception), "Not a valid text type")
        
    def test_empty_invalid_text_type(self):
        with self.assertRaises(Exception) as context:
            split_nodes_delimeter(node, "`", "test")
        self.assertEqual(str(context.exception), "Not a valid text type")

    def test_delim_not_in_text(self):
        with self.assertRaises(Exception) as context:
            split_nodes_delimeter(node3, "`", "code")
        self.assertEqual(str(context.exception), "invalid markdown syntax")
    
    def test_mixed_nodes(self):
        print(f"Results from testing a list of mixed textnodes on split nodes delim inline funct: {split_nodes_delimeter(node2, "`", "code")}")
