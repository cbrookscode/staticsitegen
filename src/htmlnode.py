
class HTMLNode:
    def __init__(self, string=None, value=None, children=None, props=None):
        self.string = string
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        #take what is in the props dictionary and turn into a string, the key will need to have a space before it, colon rpelaced with equal sign, no spaces between key and value
        test = list(map(lambda x: f" {x[0]}={x[1]}", self.props))
        print(",".join(test))
        