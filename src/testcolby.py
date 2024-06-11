# from htmlnode import HTMLNode 
# from htmlnode import LeafNode 
# from htmlnode import ParentNode 

# test_1 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
# test_2 = LeafNode("p", "This is a paragraph of text.")

# def to_html(self):
#     result = f"<{self.tag}{self.props_to_html()}>"
#     for child in self.children:
#         result += child.to_html()
#     print(result + f"</{self.tag}>")


# node = ParentNode(
#     "p",
#     [
#         LeafNode("b", "Bold text"),
#         LeafNode(None, "Normal text"),
#         LeafNode("i", "italic text"),
#         LeafNode(None, "Normal text"),
#     ],
# )

# print(node.to_html())
import re
text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
print(matches)

text2 = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
matches2 = re.findall(r"\[(.*?)\]\((.*?)\)", text2)
print(matches2)