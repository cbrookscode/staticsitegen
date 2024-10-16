from textnode import TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode

def main():

    text = "This is text with a `code block` word"
    # above produces this: ['This is text with a ', 'code block', ' word']
    split = text.split("`")
    print(split[0])
    print(split[1])
    print(split[2])

if __name__=="__main__":
    main()