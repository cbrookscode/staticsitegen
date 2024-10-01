from textnode import TextNode
from htmlnode import HTMLNode

def main():

    test = TextNode("string", "bold", "http:site")
    print(test.__repr__())

    dict = {
    "href": "https://www.google.com", 
    "target": "_blank",
    }
    testhtml = HTMLNode("apple", "a", None, dict)

    testhtml.props_to_html()

if __name__=="__main__":
    main()