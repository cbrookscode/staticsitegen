import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def testingdefault(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def testingcustom(self):
        node = HTMLNode(tag="p", value="Hello", children=[], props={"class": "text"})
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Hello")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {"class": "text"})
    
    def test_repr(self):
        node = HTMLNode(tag="p", value="Hello", children=[], props={"class": "text"})
        expected_repr = "HTMLnode(tag=p, value = Hello, children = [], props = {'class': 'text'})"
        self.assertEqual(repr(node), expected_repr)