from htmlnode import HTMLNode
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__( tag, value, None, props)
        if not value:
            raise ValueError("Value required for LeafNode")
        
    def to_html(self):
        if not self.tag:
            return self.value
        if self.props:
            return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"
        
        