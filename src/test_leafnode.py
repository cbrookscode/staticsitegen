import unittest

from leafnode import LeafNode

# Test Leafs
leaf = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
leaf2 = LeafNode("p", "This is a paragraph of text.")
leaf3 = LeafNode("", "TestValue")

class TestHTMLNode(unittest.TestCase):

    def test_normal_leaf_to_html(self):
        print(f"To Html leafnode method test with normal leaf provided: {leaf.to_html()}")

    def test_no_tag(self):
        print(f"To Html leafnode method test with no tag provided: {leaf3.to_html()}")

    def test_no_value(self):
        with self.assertRaises(ValueError) as context:
            LeafNode("p", "", {"href": "https://www.google.com"})
        self.assertEqual(str(context.exception), "Value required for LeafNode")

    def test_no_props(self):
        print(f"To Html leafnode method test with no props dict provided: {leaf3.to_html()}")

    def test_empty_leaf_construction(self):
        with self.assertRaises(ValueError) as context:
            LeafNode()
        self.assertEqual(str(context.exception), "Value required for LeafNode")
    
    def test_trying_to_put_in_children(self):
        with self.assertRaises(TypeError) as context:
            LeafNode("a", "Click me!", "b", {"href": "https://www.google.com"})

        