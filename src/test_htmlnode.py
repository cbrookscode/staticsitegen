import unittest

from htmlnode import HTMLNode

dict = {
"href": "https://www.google.com", 
"target": "_blank",
}

class TestHTMLNode(unittest.TestCase):
    def test_none(self):
        node = HTMLNode()
        self.assertIsInstance(node, HTMLNode)

    def test_only_tag(self):
        node = HTMLNode("apple")
        self.assertIsInstance(node, HTMLNode)

    def test_only_dict(self):
        node = HTMLNode(props=dict)
        self.assertIsInstance(node, HTMLNode)

    def test_diff_tag(self):
        node = HTMLNode(tag="apple", value="a", props=dict)
        node2 = HTMLNode(tag="pear", value="a", props=dict)
        self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        testhtml= HTMLNode(tag="pear", value="a", props=dict)
        result = testhtml.props_to_html()
        expected = 'href="https://www.google.com" target="_blank"'
        self.assertEqual(result, expected, f"Expected {expected} but got {result}")

    def test_props_to_html_with_no_props(self):
        node= HTMLNode(tag="pear", value="a")
        with self.assertRaises(Exception) as context:
            node.props_to_html()
        self.assertEqual(str(context.exception), "No prop dictionary provided in this HTMLNode")


    def test_repr(self):
        testhtml= HTMLNode(tag="pear", value="a", props=dict)
        result = testhtml.__repr__()
        expected = f'{HTMLNode("pear", "a", None, {'href': 'https://www.google.com', 'target': '_blank'})}'
        self.assertEqual(result, expected, f"Expected {expected} but got {result}")

    