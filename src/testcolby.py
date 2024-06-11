from htmlnode import HTMLNode 
from htmlnode import LeafNode 

test_1 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
test_2 = LeafNode("p", "This is a paragraph of text.")

def to_html(self):
    emptystring = ""
    if not self.value:
        raise ValueError("All leaf nodes require a value.")
    elif not self.tag:
        return self.value
    elif not self.props:
        print(f"<{self.tag}>{self.value}</{self.tag}>")
    print(f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>")

to_html(test_2)
to_html(test_1)
