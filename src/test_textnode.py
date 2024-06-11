import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold", "https://www.boot.dev/lessons")
        node2 = TextNode("This is a text node", "bold", "https://www.boot.dev/lessons")
        self.assertEqual(node, node2)

    def test_difftexttype(self):
        node = TextNode("This is a text node", "bold", "https://www.boot.dev/lessons")
        node2 = TextNode("This is a text node", "italics", "https://www.boot.dev/lessons")
        self.assertEqual(node, node2)

    def test_nonstring(self):
        node = TextNode(10, "bold", "https://www.boot.dev/lessons")
        node2 = TextNode("This is a text node", "bold", "https://www.boot.dev/lessons")
        self.assertEqual(node, node2)

    def test_bothnonstring(self):
        node = TextNode(10, "bold", "https://www.boot.dev/lessons")
        node2 = TextNode(10, "bold", "https://www.boot.dev/lessons")
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()