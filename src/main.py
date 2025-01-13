from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    node = TextNode("Test Text", TextType.ITALIC, "Test URL")
    #node = HTMLNode("p", "TEST", ["object1", "object2"], {"href": "https://www.google.com", "target": "_blank"})
    print(node)

if __name__ == "__main__":
    main()