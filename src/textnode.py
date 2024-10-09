class TextNode:
    def __init__(self, TEXT, TEXT_TYPE, URL=None):
        self.text = TEXT
        self.text_type = TEXT_TYPE
        self.url = URL

    # determine if two textnodes are the same
    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    # represent textnode as a string
    def __repr__(self):
        return f"{type(self).__name__}({self.text}, {self.text_type}, {self.url})"