from textnode import TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode

def main():

    text = "This is text with a `code block` word"
    print(text.split("`"))

if __name__=="__main__":
    main()