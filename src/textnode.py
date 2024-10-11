from leafnode import LeafNode

formats = ["text", "bold", "italic", "code", "link", "image"]

class TextNode:
    def __init__(self, TEXT, TEXT_TYPE, URL=None):
        self.text = TEXT
        self.text_type = TEXT_TYPE
        self.url = URL

        if self.text_type not in formats:
            raise Exception("Text type is not supported. Supported types are text, bold, italic, code, link, image.")

    # determine if two textnodes are the same
    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    # represent textnode as a string
    def __repr__(self):
        return f"{type(self).__name__}({self.text}, {self.text_type}, {self.url})"
    
    def text_node_to_html_node(self):
        if self.text_type == "text":
            return LeafNode(value=self.text)
        if self.text_type == "bold":
            return LeafNode("b", self.text)
        if self.text_type == "italic":
            return LeafNode("i", self.text)
        if self.text_type == "code":
            return LeafNode("code", self.text)
        if self.text_type == "link":
            return LeafNode("a", self.text, {"href": self.url})
        if self.text_type == "image":
            return LeafNode("img", "", {"src": self.url, "alt": self.text})
        raise Exception("Text type doesn't match supported formats.")