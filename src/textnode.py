class TextNode:
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type 
        self.url = url
    
    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return (other.text == self.text and 
                other.text_type == self.text_type and 
                other.url == self.url)
    
    def __repr__(self):
        return f'TextNode({self.text!r}, {self.text_type!r}, {self.url!r})'