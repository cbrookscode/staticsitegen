from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__( tag, None, children, props)
        if not children:
            raise ValueError("ParentNode must have children.")
        if not self.tag:
            raise ValueError("Parent must have a tag")
        self.children = children

    def to_html(self):
        html = ""
        if self.props:
            html += self.props_to_html()
        for child in self.children:
            test = child
            html += child.to_html()
        return f"<{self.tag}>{html}</{self.tag}>"
