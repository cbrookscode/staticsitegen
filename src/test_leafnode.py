import unittest

from leafnode import LeafNode

# Test Leafs
leaf = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
leaf2 = LeafNode("p", "This is a paragraph of text.")
leaf3 = LeafNode("", "TestValue")

class TestHTMLNode(unittest.TestCase):

    def test_normal_leaf_to_html(self):
        result = leaf.to_html()
        expected = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(result, expected, f"Expected {expected} but got {result}")

    def test_no_tag(self):
        result = leaf3.to_html()
        expected = "TestValue"
        self.assertEqual(result, expected, f"Expected {expected} but got {result}")

    def test_no_value(self):
        with self.assertRaises(ValueError) as context:
            LeafNode("p", None, {"href": "https://www.google.com"})
        self.assertEqual(str(context.exception), "Value required for LeafNode")

    def test_no_props(self):
        result = leaf3.to_html()
        expected = "TestValue"
        self.assertEqual(result, expected, f"Expected {expected} but got {result}")

    def test_empty_leaf_construction(self):
        with self.assertRaises(ValueError) as context:
            LeafNode()
        self.assertEqual(str(context.exception), "Value required for LeafNode")
    
    def test_trying_to_put_in_children(self):
        with self.assertRaises(TypeError) as context:
            LeafNode("a", "Click me!", "b", {"href": "https://www.google.com"})

        