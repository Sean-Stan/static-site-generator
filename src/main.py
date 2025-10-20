from textnode import TextNode, TextType

def main():
    tester = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(tester)

main()