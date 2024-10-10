from textnode import TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode

def main():

    node = ParentNode(
        "p",
        [   
            LeafNode("b", "Bold text"),
            ParentNode("p", [LeafNode(None, "nested leaf in parent")],),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )
    

    print(node.to_html())

if __name__=="__main__":
    main()