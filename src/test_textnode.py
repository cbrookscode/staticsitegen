import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_url_non(self):
        node = TextNode("This is a text node", "bold", None)
        node2 = TextNode("This is a text node", "bold", None)
        self.assertEqual(node, node2)

    def test_url_none_2(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold", None)
        self.assertEqual(node, node2)

    def test_different_textype(self):
        node = TextNode("This is a text node", "italic", None)
        node2 = TextNode("This is a text node", "bold", None)
        self.assertNotEqual(node, node2)

    def test_diff_text(self):
        node = TextNode("This is a testy text node", "bold", None)
        node2 = TextNode("This is a text node", "bold", None)
        self.assertNotEqual(node, node2)

    def test_empty_text(self):
        node = TextNode("", "bold")
        node2 = TextNode("", "bold")
        self.assertEqual(node, node2)
        
    def test_empty_type(self):
        node = TextNode("This is a text node", "")
        node2 = TextNode("This is a text node", "")
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()