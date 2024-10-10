import unittest

from parentnode import ParentNode
from leafnode import LeafNode

node = ParentNode(
    "p",
    [   
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)

node2 = ParentNode(
    "p",
    [   
        LeafNode("b", "Bold text"),
        ParentNode("p", [LeafNode(None, "second level")],),
        ParentNode(
        "p",
        [        
        LeafNode(None, "3rd level"),
        LeafNode("i", "italic text"),
        LeafNode(None, "3rd level"),
        ],
        )
    ],
)

node3 = ParentNode(
    "p",
    [   
        LeafNode("b", "Bold text"),
        ParentNode("p", [LeafNode(None, "second level")], {"href": "https://www.test.com"}),
        ParentNode(
        "p",
        [        
        LeafNode(None, "3rd level"),
        LeafNode("i", "italic text", {"href": "https://www.google.com"}),
        LeafNode(None, "3rd level"),
        ],
        )
    ],
{"href": "https://www.test2.com"}
)




class TestHTMLNode(unittest.TestCase):

    def test_standard_parent_with_only_leaf_children(self):
        print(f"Test standard parent with only leaf children to html method: {node.to_html()}")

    def test_nested_parent_nodes_along_with_leaf_children(self):
        print(f"Test parent to html method with nested parents in children: {node2.to_html()}")
    
    def test_no_children(self):
        with self.assertRaises(ValueError) as context:
            ParentNode("p")

    def test_no_tag_on_parent_but_has_children(self):
        with self.assertRaises(ValueError) as context:
            ParentNode(children=[LeafNode(None, "Normal text")],)

    def test_blank_parent(self):
        with self.assertRaises(ValueError) as context:
            ParentNode()

    def test_parent_node_with_nested_props(self):
        print(f"Test having props nested in parent: {node3.to_html()}")
