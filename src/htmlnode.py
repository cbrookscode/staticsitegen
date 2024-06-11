

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        sentence = ""
        for key, value in self.props.items():
            sentence += f" {key}=\"{value}\""
        return sentence
    
    def __repr__(self):
        return f"HTMLnode(tag={self.tag}, value = {self.value}, children = {self.children}, props = {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        # Ensure that 'value' is not None
        if value is None:
            raise ValueError("LeafNode requires a value.")
        # call parent constructor
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        emptystring = ""
        if not self.value:
            raise ValueError("All leaf nodes require a value.")
        elif not self.tag:
            return self.value
        elif not self.props:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            for key, value in self.props.items():
                emptystring += f"<{self.tag}> {key}=\"{value}\">{self.value}</{self.tag}>"
            return emptystring