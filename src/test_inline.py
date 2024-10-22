from textnode import TextNode
from inline import split_nodes_delimeter, split_nodes_images, split_nodes_links, extract_markdown_images, extract_markdown_links, text_to_textnodes

import unittest

node = [TextNode("This is text with a `code block` word", "text"), TextNode("testing", "italic")]
node2 = [TextNode("This is text `with` a word", "text"), TextNode("testing", "text"), TextNode("how *now* brown cow", "italic")]
node3 = [TextNode("This is text **with** a word", "text"), TextNode("testing", "text"), TextNode("how *now* brown cow", "text")]
node4 = [TextNode("This is text *with** a word", "text"), TextNode("testing", "text"), TextNode("how *now* brown cow", "italic")]

class TestSplitwDelimeter(unittest.TestCase):
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
        print(f"This is delim not in text: {split_nodes_delimeter(node3, "*", "italic")}")
    
    def test_mixed_nodes(self):
        print(f"This is test mixed nodes: {split_nodes_delimeter(node2, "`", "code")}")


    def test_incorrect_markdown(self):
        print(f"this is test incorrect markdown: {split_nodes_delimeter(node4, "*", "italic")}")






# extract image from markdown test variables
test_image = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
test_image2 = "This is text with a !rick roll](https://i.imgur.com/aKaOqIh.gif and ![obi wan(https://i.imgur.com/fJRm4Vk.jpeg"
test_image3 = "This is text with a test![rick roll](https://i.imgur.com/aKaOqIh.gif) and test![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
test_image4 = "This is text with a ![rick roll]test(https://i.imgur.com/aKaOqIh.gif) and ![obi wan]test(https://i.imgur.com/fJRm4Vk.jpeg)"
test_image5 = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)test and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)test"

class TestExtrackingImages(unittest.TestCase):

    def test_extracting_images_normal(self):
        result = extract_markdown_images(test_image)
        expected = [('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')]
        self.assertEqual(result, expected, f"Expected {expected} but got {result}")

    def test_extracting_images_text_in_front(self):
        result = extract_markdown_images(test_image3)
        expected = [('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')]
        self.assertEqual(result, expected, f"Expected {expected} but got {result}")

    def test_extracting_images_text_in_between(self):
        result = extract_markdown_images(test_image4)
        expected = []
        self.assertEqual(result, expected, f"Expected {expected} but got {result}")

    def test_extracting_images_text_afterwards(self):
        result = extract_markdown_images(test_image5)
        expected = [('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')]
        self.assertEqual(result, expected, f"Expected {expected} but got {result}")

    def test_extracting_images_no_match(self):
        result = extract_markdown_images(test_image2)
        expected = []
        self.assertEqual(result, expected, f"Expected {expected} but got {result}")



#extract links from markdown test variables
test_link = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
test_link2 = "This is text with a link test[to boot dev](https://www.boot.dev) and test[to youtube](https://www.youtube.com/@bootdotdev)"
test_link3 = "This is text with a link [to boot dev]test(https://www.boot.dev) and [to youtube]test(https://www.youtube.com/@bootdotdev)"
test_link4 = "This is text with a link [to boot dev](https://www.boot.dev)test and [to youtube](https://www.youtube.com/@bootdotdev)test"
test_link5 = "This is text with a link [to boot dev(https://www.boot.dev and to youtube]https://www.youtube.com/@bootdotde"

class TestExtrackingLinks(unittest.TestCase):
    def test_extracting_links_normal(self):
        result = extract_markdown_links(test_link)
        expected = [('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')]
        self.assertEqual(result, expected, f"Expected {expected} but got {result}")

    def test_extracting_links_text_in_front(self):
        result = extract_markdown_links(test_link2)
        expected = [('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')]
        self.assertEqual(result, expected, f"Expected {expected} but got {result}")

    def test_extracting_links_text_in_between(self):
        result = extract_markdown_links(test_link3)
        expected = []
        self.assertEqual(result, expected, f"Expected {expected} but got {result}")

    def test_extracting_links_text_afterwards(self):
        result = extract_markdown_links(test_link4)
        expected = [('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')]
        self.assertEqual(result, expected, f"Expected {expected} but got {result}")

    def test_extracting_links_no_match(self):
        result = extract_markdown_links(test_link5)
        expected = []
        self.assertEqual(result, expected, f"Expected {expected} but got {result}")



# split_nodes_images
split_images = [
    TextNode("This is text with a image ![to boot dev](https://i.imgur.com/aKaOqIh.gif) and ![to youtube](https://i.imgur.com/fJRm4Vk.jpeg)", "text",), 
    TextNode("This is text2 with a image2 ![to boot dev2](https://i.imgur.com/aKaOqIh.gif2) and2 ![to youtube2](https://i.imgur.com/fJRm4Vk.jpeg2)", "text",)
    ]

split_images_empty = []

split_images_no_images = [
    TextNode("This is text with no image  and nothing.", "text",), 
    TextNode("This is text2 with nothing and2 nothing!!", "code",)
    ]

split_images_nontext_textnode = [
    TextNode("This is text with a image ![to boot dev](https://i.imgur.com/aKaOqIh.gif) and ![to youtube](https://i.imgur.com/fJRm4Vk.jpeg)", "code",), 
    TextNode("This is text2 with a image2 ![to boot dev2](https://i.imgur.com/aKaOqIh.gif2) and2 ![to youtube2](https://i.imgur.com/fJRm4Vk.jpeg2)", "italic",)
    ]

split_images_mixed_texttypes = [
    TextNode("This is text with a image ![to boot dev](https://i.imgur.com/aKaOqIh.gif) and ![to youtube](https://i.imgur.com/fJRm4Vk.jpeg)", "text",), 
    TextNode("This is text2 with a image2 ![to boot dev2](https://i.imgur.com/aKaOqIh.gif2) and2 ![to youtube2](https://i.imgur.com/fJRm4Vk.jpeg2)", "code",)
    ]

split_images_no_excalamation = [
    TextNode("This is text with a image [to boot dev](https://i.imgur.com/aKaOqIh.gif) and [to youtube](https://i.imgur.com/fJRm4Vk.jpeg)", "text",), 
    TextNode("This is text2 with a image2 [to boot dev2](https://i.imgur.com/aKaOqIh.gif2) and2 [to youtube2](https://i.imgur.com/fJRm4Vk.jpeg2)", "code",)
    ]

class TestSplitImages(unittest.TestCase):
    def test_split_nodes_images_normal(self):
        result = split_nodes_images(split_images)
        expected = [
        TextNode("This is text with a image ", "text", None),
        TextNode("to boot dev", "image", "https://i.imgur.com/aKaOqIh.gif"),
        TextNode(" and ", "text", None),
        TextNode("to youtube", "image", "https://i.imgur.com/fJRm4Vk.jpeg"),
        TextNode("This is text2 with a image2 ", "text", None),
        TextNode("to boot dev2", "image", "https://i.imgur.com/aKaOqIh.gif2"),
        TextNode(" and2 ", "text", None),
        TextNode("to youtube2", "image", "https://i.imgur.com/fJRm4Vk.jpeg2")
        ]        
        self.assertEqual(result, expected, f"Expected {expected} but got {result}")

    def test_split_nodes_images_empty_textnode(self):
        with self.assertRaises(Exception) as context:
            split_nodes_images(split_images_empty)
        self.assertEqual(str(context.exception), "Cannot provide an empty node list")

    def test_split_images_no_images(self):
        result = split_nodes_images(split_images_no_images)
        expected = [
        TextNode("This is text with no image  and nothing.", "text", None),
        TextNode("This is text2 with nothing and2 nothing!!", "code", None)
        ]
        self.assertEqual(result, expected, f"Expected {expected} but got {result}")

    def test_split_images_nontext_textnode(self):
        result = split_nodes_images(split_images_nontext_textnode)
        expected = [
        TextNode("This is text with a image ![to boot dev](https://i.imgur.com/aKaOqIh.gif) and ![to youtube](https://i.imgur.com/fJRm4Vk.jpeg)", "code", None),
        TextNode("This is text2 with a image2 ![to boot dev2](https://i.imgur.com/aKaOqIh.gif2) and2 ![to youtube2](https://i.imgur.com/fJRm4Vk.jpeg2)", "italic", None)
        ]
        self.assertEqual(result, expected, f"Expected {expected} but got {result}")

    def test_split_images_empty_texttype(self):
        with self.assertRaises(Exception) as context:
            split_nodes_images([TextNode("This is text with a image ![to boot dev](https://i.imgur.com/aKaOqIh.gif) and ![to youtube](https://i.imgur.com/fJRm4Vk.jpeg)", "",), TextNode("This is text2 with a image2 ![to boot dev2](https://i.imgur.com/aKaOqIh.gif2) and2 ![to youtube2](https://i.imgur.com/fJRm4Vk.jpeg2)", "",)])
        self.assertEqual(str(context.exception), "Text type is not supported. Supported types are text, bold, italic, code, link, image.")

    def test_split_images_mixed_texttypes(self):
        result = split_nodes_images(split_images_mixed_texttypes)
        expected = [
        TextNode("This is text with a image ", "text", None),
        TextNode("to boot dev", "image", "https://i.imgur.com/aKaOqIh.gif"),
        TextNode(" and ", "text", None),
        TextNode("to youtube", "image", "https://i.imgur.com/fJRm4Vk.jpeg"),
        TextNode("This is text2 with a image2 ![to boot dev2](https://i.imgur.com/aKaOqIh.gif2) and2 ![to youtube2](https://i.imgur.com/fJRm4Vk.jpeg2)", "code", None)
        ]
        self.assertEqual(result, expected, f"Expected {expected} but got {result}")

    def test_split_images_no_excalamation(self):
        result = split_nodes_images(split_images_no_excalamation)
        expected = [
        TextNode("This is text with a image [to boot dev](https://i.imgur.com/aKaOqIh.gif) and [to youtube](https://i.imgur.com/fJRm4Vk.jpeg)", "text", None),
        TextNode("This is text2 with a image2 [to boot dev2](https://i.imgur.com/aKaOqIh.gif2) and2 [to youtube2](https://i.imgur.com/fJRm4Vk.jpeg2)", "code", None)
        ]
        self.assertEqual(result, expected, f"Expected {expected} but got {result}")



#split_nodes_links
split_links = [
    TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", "text",), 
    TextNode("This is text2 with a link2 [to boot dev2](https://www.boot.dev2) and2 [to youtube2](https://www.youtube.com/@bootdotdev2)", "text",)
    ]

split_links_empty = []

split_links_no_links = [
    TextNode("This is text with no link and nothing.", "text",), 
    TextNode("This is text2 with nothing and2 nothing!!", "code",)
    ]

split_links_nontext_textnode = [
    TextNode("This is text with a links ![to boot dev](https://i.imgur.com/aKaOqIh.gif) and ![to youtube](https://i.imgur.com/fJRm4Vk.jpeg)", "code",), 
    TextNode("This is text2 with a links2 ![to boot dev2](https://i.imgur.com/aKaOqIh.gif2) and2 ![to youtube2](https://i.imgur.com/fJRm4Vk.jpeg2)", "italic",)
    ]

split_links_mixed_texttypes = [
    TextNode("This is text with a link[to boot dev](https://i.imgur.com/aKaOqIh.gif) and [to youtube](https://i.imgur.com/fJRm4Vk.jpeg)", "text",), 
    TextNode("This is text2 with a link2 [to boot dev2](https://i.imgur.com/aKaOqIh.gif2) and2 [to youtube2](https://i.imgur.com/fJRm4Vk.jpeg2)", "code",)
    ]

split_links_with_exclamations = [
    TextNode("This is text with a link ![to boot dev](https://i.imgur.com/aKaOqIh.gif) and ![to youtube](https://i.imgur.com/fJRm4Vk.jpeg)", "text",), 
    TextNode("This is text2 with a ilink2 ![to boot dev2](https://i.imgur.com/aKaOqIh.gif2) and2 ![to youtube2](https://i.imgur.com/fJRm4Vk.jpeg2)", "text",)
    ]

split_links_mixed_weirdness = [
    TextNode("This is text with a link [to boot dev](https://i.imgur.com/aKaOqIh.gif) and [to youtube](https://i.imgur.com/fJRm4Vk.jpeg)", "text",), 
    TextNode("This is text2 with a ilink2 ![to boot dev2](https://i.imgur.com/aKaOqIh.gif2) and2 ![to youtube2](https://i.imgur.com/fJRm4Vk.jpeg2)", "code",),
    TextNode("This is text with no link and nothing.", "text",),
    TextNode("This is text2 with a ilink2 and2 ![to youtube2](https://i.imgur.com/fJRm4Vk.jpeg2)", "text",),
    "",
    ]


class TestSplitLinks(unittest.TestCase):
    def test_split_links_normal(self):
        result = split_nodes_links(split_links)
        expected = [
        TextNode("This is text with a link ", "text", None),
        TextNode("to boot dev", "link", "https://www.boot.dev"),
        TextNode(" and ", "text", None),
        TextNode("to youtube", "link", "https://www.youtube.com/@bootdotdev"),
        TextNode("This is text2 with a link2 ", "text", None),
        TextNode("to boot dev2", "link", "https://www.boot.dev2"),
        TextNode(" and2 ", "text", None),
        TextNode("to youtube2", "link", "https://www.youtube.com/@bootdotdev2")
        ]
        self.assertEqual(result, expected, f"Expected {expected} but got {result}")
    
    def test_split_links_empty_list(self):
        with self.assertRaises(Exception) as context:
            split_nodes_links(split_links_empty)
        self.assertEqual(str(context.exception), "Cannot provide an empty node list")

    def test_split_links_no_links(self):
        result = split_nodes_links(split_links_no_links)
        expected = [
        TextNode("This is text with no link and nothing.", "text", None),
        TextNode("This is text2 with nothing and2 nothing!!", "code", None)
        ]
        self.assertEqual(result, expected, f"Expected {expected} but got {result}")
    
    def test_split_links_none_text_textnode(self):
        result = split_nodes_links(split_links_nontext_textnode)
        expected = [
        TextNode("This is text with a links ![to boot dev](https://i.imgur.com/aKaOqIh.gif) and ![to youtube](https://i.imgur.com/fJRm4Vk.jpeg)", "code", None),
        TextNode("This is text2 with a links2 ![to boot dev2](https://i.imgur.com/aKaOqIh.gif2) and2 ![to youtube2](https://i.imgur.com/fJRm4Vk.jpeg2)", "italic", None)
        ]
        self.assertEqual(result, expected, f"Expected {expected} but got {result}")
    
    def test_split_links_mixed_texttypes(self):
        result = split_nodes_links(split_links_mixed_texttypes)
        expected = [
        TextNode("This is text with a link", "text", None),
        TextNode("to boot dev", "link", "https://i.imgur.com/aKaOqIh.gif"),
        TextNode(" and ", "text", None),
        TextNode("to youtube", "link", "https://i.imgur.com/fJRm4Vk.jpeg"),
        TextNode("This is text2 with a link2 [to boot dev2](https://i.imgur.com/aKaOqIh.gif2) and2 [to youtube2](https://i.imgur.com/fJRm4Vk.jpeg2)", "code", None)
        ]
        self.assertEqual(result, expected, f"Expected {expected} but got {result}")

    def test_split_links_with_excalmations(self):
        result = split_nodes_links(split_links_with_exclamations)
        expected = [
        TextNode("This is text with a link ![to boot dev](https://i.imgur.com/aKaOqIh.gif) and ![to youtube](https://i.imgur.com/fJRm4Vk.jpeg)", "text", None),
        TextNode("This is text2 with a ilink2 ![to boot dev2](https://i.imgur.com/aKaOqIh.gif2) and2 ![to youtube2](https://i.imgur.com/fJRm4Vk.jpeg2)", "text", None)
        ]
        self.assertEqual(result, expected, f"Expected {expected} but got {result}")

    def test_split_links_mix_weirdness(self):
        result = split_nodes_links(split_links_mixed_weirdness)
        expected = [
        TextNode("This is text with a link ", "text", None),
        TextNode("to boot dev", "link", "https://i.imgur.com/aKaOqIh.gif"),
        TextNode(" and ", "text", None),
        TextNode("to youtube", "link", "https://i.imgur.com/fJRm4Vk.jpeg"),
        TextNode("This is text2 with a ilink2 ![to boot dev2](https://i.imgur.com/aKaOqIh.gif2) and2 ![to youtube2](https://i.imgur.com/fJRm4Vk.jpeg2)", "code", None),
        TextNode("This is text with no link and nothing.", "text", None),
        TextNode("This is text2 with a ilink2 and2 ![to youtube2](https://i.imgur.com/fJRm4Vk.jpeg2)", "text", None)
        ]
        self.assertEqual(result, expected, f"Expected {expected} but got {result}")



class TestMarkdowntoTextNodes(unittest.TestCase):
    def test_markdown_to_textnodes_standard(self):
        Markdown_text = "This is **text** with an *italic* word **and** a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev) and more **text** with an *italic* word **and** a `code block` and an"
        result = text_to_textnodes(Markdown_text)
        expected = [
        TextNode("This is ", "text", None),
        TextNode("text", "bold", None),
        TextNode(" with an ", "text", None),
        TextNode("italic", "italic", None),
        TextNode(" word ", "text", None),
        TextNode("and", "bold", None),
        TextNode(" a ", "text", None),
        TextNode("code block", "code", None),
        TextNode(" and an ", "text", None),
        TextNode("obi wan image", "image", "https://i.imgur.com/fJRm4Vk.jpeg"),
        TextNode(" and a ", "text", None),
        TextNode("link", "link", "https://boot.dev"),
        TextNode("text", "bold", None),
        TextNode(" with an ", "text", None),
        TextNode("italic", "italic", None),
        TextNode(" word ", "text", None),
        TextNode("and", "bold", None),
        TextNode(" a ", "text", None),
        TextNode("code block", "code", None),
        TextNode(" and an", "text", None)
        ]
        self.assertEqual(result, expected, f"Expected {expected} but got {result}")

    def test_markdown_to_textnodes_standard_2(self):
        Markdown_text = "This is **text** with an *italic* word **and** a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev) and more **text** with an *italic* word **and** a `code block` and an!!!! Beepoperino Jambrino"
        result = text_to_textnodes(Markdown_text)
        expected = [
        TextNode("This is ", "text", None),
        TextNode("text", "bold", None),
        TextNode(" with an ", "text", None),
        TextNode("italic", "italic", None),
        TextNode(" word ", "text", None),
        TextNode("and", "bold", None),
        TextNode(" a ", "text", None),
        TextNode("code block", "code", None),
        TextNode(" and an ", "text", None),
        TextNode("obi wan image", "image", "https://i.imgur.com/fJRm4Vk.jpeg"),
        TextNode(" and a ", "text", None),
        TextNode("link", "link", "https://boot.dev"),
        TextNode("text", "bold", None),
        TextNode(" with an ", "text", None),
        TextNode("italic", "italic", None),
        TextNode(" word ", "text", None),
        TextNode("and", "bold", None),
        TextNode(" a ", "text", None),
        TextNode("code block", "code", None),
        TextNode(" and an!!!! Beepoperino Jambrino", "text", None)
        ]
        self.assertEqual(result, expected, f"Expected {expected} but got {result}")

    def test_markdown_to_textnodes_only_text(self):
        Markdown_text = "Hi Hellow, heee xp. Weee me bee thee. Steve!"
        result = text_to_textnodes(Markdown_text)
        expected = [TextNode("Hi Hellow, heee xp. Weee me bee thee. Steve!", "text", None)]
        self.assertEqual(result, expected, f"Expected {expected} but got {result}")

    def test_markdown_to_textnodes_no_text(self):
        Markdown_text = ""
        with self.assertRaises(Exception) as context:
            text_to_textnodes(Markdown_text)
        self.assertEqual(str(context.exception), "No text provided to convert")
    
    def test_markdown_to_textnodes_incorrect_markdown(self):
        Markdown_text = "Hiya *I cannot write Markdown at all** whooohoo.!"
        print(text_to_textnodes(Markdown_text))
