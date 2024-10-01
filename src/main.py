from textnode import TextNode

def main():

    test = TextNode("string", "bold", "http:site")
    print(test.__repr__())

if __name__=="__main__":
    main()