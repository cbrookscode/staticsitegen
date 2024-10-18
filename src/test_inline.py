from textnode import TextNode
from inline import split_nodes_delimeter, split_nodes_images, split_nodes_links, extract_markdown_images, extract_markdown_links

import unittest

# split_nodes_delimeter(old_nodes, delimiter, text_type)

node = [TextNode("This is text with a `code block` word", "text"), TextNode("testing", "italic")]
node2 = [TextNode("This is text `with` a word", "text"), TextNode("testing", "text"), TextNode("how *now* brown cow", "italic")]
node3 = [TextNode("This is text **with** a word", "text"), TextNode("testing", "text"), TextNode("how *now* brown cow", "italic")]

# extract image from markdown test variables
test_image = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
test_image2 = "This is text with a !rick roll](https://i.imgur.com/aKaOqIh.gif and ![obi wan(https://i.imgur.com/fJRm4Vk.jpeg"
test_image3 = "This is text with a test![rick roll](https://i.imgur.com/aKaOqIh.gif) and test![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
test_image4 = "This is text with a ![rick roll]test(https://i.imgur.com/aKaOqIh.gif) and ![obi wan]test(https://i.imgur.com/fJRm4Vk.jpeg)"
test_image5 = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)test and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)test"

#extract links from markdown test variables
test_link = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
test_link2 = "This is text with a link test[to boot dev](https://www.boot.dev) and test[to youtube](https://www.youtube.com/@bootdotdev)"
test_link3 = "This is text with a link [to boot dev]test(https://www.boot.dev) and [to youtube]test(https://www.youtube.com/@bootdotdev)"
test_link4 = "This is text with a link [to boot dev](https://www.boot.dev)test and [to youtube](https://www.youtube.com/@bootdotdev)test"
test_link5 = "This is text with a link [to boot dev(https://www.boot.dev and to youtube]https://www.youtube.com/@bootdotde"

# split_nodes_images
split_images = [
    TextNode("This is text with a image ![to boot dev](https://i.imgur.com/aKaOqIh.gif) and ![to youtube](https://i.imgur.com/fJRm4Vk.jpeg)", "text",), 
    TextNode("This is text2 with a image2 ![to boot dev2](https://i.imgur.com/aKaOqIh.gif2) and2 ![to youtube2](https://i.imgur.com/fJRm4Vk.jpeg2)", "text",)
    ]
split_images_empty = [
    TextNode("This is text with a image ![to boot dev](https://i.imgur.com/aKaOqIh.gif) and ![to youtube](https://i.imgur.com/fJRm4Vk.jpeg)", "text",), 
    TextNode("This is text2 with a image2 ![to boot dev2](https://i.imgur.com/aKaOqIh.gif2) and2 ![to youtube2](https://i.imgur.com/fJRm4Vk.jpeg2)", "text",)
    ]
split_images_no_images = [
    TextNode("This is text with a image ![to boot dev](https://i.imgur.com/aKaOqIh.gif) and ![to youtube](https://i.imgur.com/fJRm4Vk.jpeg)", "text",), 
    TextNode("This is text2 with a image2 ![to boot dev2](https://i.imgur.com/aKaOqIh.gif2) and2 ![to youtube2](https://i.imgur.com/fJRm4Vk.jpeg2)", "text",)
    ]
split_images_nontext_textnode = [
    TextNode("This is text with a image ![to boot dev](https://i.imgur.com/aKaOqIh.gif) and ![to youtube](https://i.imgur.com/fJRm4Vk.jpeg)", "code",), 
    TextNode("This is text2 with a image2 ![to boot dev2](https://i.imgur.com/aKaOqIh.gif2) and2 ![to youtube2](https://i.imgur.com/fJRm4Vk.jpeg2)", "italic",)
    ]
split_images_empty_texttype = [
    TextNode("This is text with a image ![to boot dev](https://i.imgur.com/aKaOqIh.gif) and ![to youtube](https://i.imgur.com/fJRm4Vk.jpeg)", "text",), 
    TextNode("This is text2 with a image2 ![to boot dev2](https://i.imgur.com/aKaOqIh.gif2) and2 ![to youtube2](https://i.imgur.com/fJRm4Vk.jpeg2)", "text",)
    ]
split_images_mixed_texttypes = [
    TextNode("This is text with a image ![to boot dev](https://i.imgur.com/aKaOqIh.gif) and ![to youtube](https://i.imgur.com/fJRm4Vk.jpeg)", "text",), 
    TextNode("This is text2 with a image2 ![to boot dev2](https://i.imgur.com/aKaOqIh.gif2) and2 ![to youtube2](https://i.imgur.com/fJRm4Vk.jpeg2)", "text",)
    ]

#split_nodes_links
split_links = [
    TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", "text",), 
    TextNode("This is text2 with a link2 [to boot dev2](https://www.boot.dev2) and2 [to youtube2](https://www.youtube.com/@bootdotdev2)", "text",)
    ]

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


    # Tests for extracking images
    def test_extracting_images_normal(self):
        print(f"Extracking Images from markdown test normal: {extract_markdown_images(test_image)}")

    def test_extracting_images_text_in_front(self):
        print(f"Extracking Images from markdown test text in front: {extract_markdown_images(test_image3)}")

    def test_extracting_images_text_in_between(self):
        print(f"Extracking Images from markdown test text in between: {extract_markdown_images(test_image4)}")

    def test_extracting_images_text_afterwards(self):
        print(f"Extracking Images from markdown test text afterwards: {extract_markdown_images(test_image5)}")

    def test_extracting_images_no_match(self):
        print(f"Extracking Images from markdown test text no match: {extract_markdown_images(test_image2)}")

    # Tests for extracting links
    def test_extracting_links_normal(self):
        print(f"Extracking links from markdown test normal: {extract_markdown_links(test_link)}")

    def test_extracting_links_text_in_front(self):
        print(f"Extracking links from markdown test text in front: {extract_markdown_links(test_link2)}")

    def test_extracting_links_text_in_between(self):
        print(f"Extracking links from markdown test text in between: {extract_markdown_links(test_link3)}")

    def test_extracting_links_text_afterwards(self):
        print(f"Extracking links from markdown test text afterwards: {extract_markdown_links(test_link4)}")

    def test_extracting_links_no_match(self):
        print(f"Extracking links from markdown test text no match: {extract_markdown_links(test_link5)}")


    # Tests for split nodes images
    def test_split_nodes_images_normal(self):
        print(f"Split nodes images normal: {split_nodes_images(split_images)}")

    # Tests for split nodes links
    def test_split_nodes_links_normal(self):
        print(f"Split nodes links normal: {split_nodes_links(split_links)}")    