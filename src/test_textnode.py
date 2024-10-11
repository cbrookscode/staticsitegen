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
        with self.assertRaises(Exception) as context:
            TextNode("This is a text node", "")

    # Testing textnode to html methods with various text types
    def test_text_text_type(self):
        node = TextNode("This is a text node", "text")
        new_leaf = node.text_node_to_html_node()
        print(f"Testing textnode to htmlnode with (text) text type: {new_leaf.to_html()}")

    def test_bold_text_type(self):
        node = TextNode("This is a text node", "bold")
        new_leaf = node.text_node_to_html_node()
        print(f"Testing textnode to htmlnode with (bold) text type: {new_leaf.to_html()}")

    def test_italic_text_type(self):
        node = TextNode("This is a text node", "italic")
        new_leaf = node.text_node_to_html_node()
        print(f"Testing textnode to htmlnode with (italic) text type: {new_leaf.to_html()}")

    def test_code_text_type(self):
        node = TextNode("This is a text node", "code")
        new_leaf = node.text_node_to_html_node()
        print(f"Testing textnode to htmlnode with (code) text type: {new_leaf.to_html()}")

    def test_link_text_type(self):
        node = TextNode("this is a link", "link", "https://google.com")
        new_leaf = node.text_node_to_html_node()
        print(f"Testing textnode to htmlnode with (link) text type: {new_leaf.to_html()}")

    def test_image_text_type(self):
        node = TextNode("This is an image", "image", "https://image.com")
        new_leaf = node.text_node_to_html_node()
        print(f"Testing textnode to htmlnode with (image) text type: {new_leaf.to_html()}")
        
if __name__ == "__main__":
    unittest.main()