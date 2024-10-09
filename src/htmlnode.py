
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    #return dictionary as a string
    def props_to_html(self):
        if not self.props:
            raise Exception("No prop dictionary provided in this HTMLNode")
        test = list(map(lambda kv: f'{kv[0]}="{kv[1]}"', self.props.items()))
        return(" ".join(test))
    
    #return string representation of HTMLNode
    def __repr__(self):
        return f"{type(self).__name__}({self.tag}, {self.value}, {self.children}, {self.props})"
        
        