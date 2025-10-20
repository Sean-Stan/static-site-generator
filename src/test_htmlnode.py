import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    link = HTMLNode(
        tag="a",
        value="Google",
        props={"href": "https://www.google.com", "target": "_blank"}
    )

    paragraph = HTMLNode(
        tag="p",
        value="Hello, world!"
    )

    div = HTMLNode(
        tag="div",
        children=[paragraph],
        props={"class": "container"}
    )

    button = HTMLNode(
        tag="button",
        value="Click me",
        props={"class": "btn btn-primary", "type": "button"}
    )

    li1 = HTMLNode(tag="li", value="Item 1")
    li2 = HTMLNode(tag="li", value="Item 2")
    ul = HTMLNode(tag="ul", children=[li1, li2])

    bold = HTMLNode(tag="b", value="bold text")
    italic = HTMLNode(tag="i", value="italic text")
    paragraph = HTMLNode(tag="p", children=[bold, italic])

    def test_props_to_html(self):
        link = HTMLNode(
            tag="a",
            value="Google",
            props={"href": "https://www.google.com", "target": "_blank"}
        )
        result = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(link.props_to_html(), result)

    def test_props_to_html2(self):
        paragraph = HTMLNode(
            tag="p",
            value="Hello, world!"
        )
        div = HTMLNode(
            tag="div",
            children=[paragraph],
            props={"class": "container"}
        )
        result = ' class="container"'
        self.assertEqual(div.props_to_html(), result)

    def test_props_to_html3(self):
        button = HTMLNode(
            tag="button",
            value="Click me",
            props={"class": "btn btn-primary", "type": "button"}
        )
        result = ' class="btn btn-primary" type="button"'
        self.assertEqual(button.props_to_html(), result)

    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )
        
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )
        
    def test_leaf_to_html_blank(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception), "All leaf nodes MUST have a value")
        
    def test_leaf_to_html_blank2(self):
        node = LeafNode(None, value="Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )





if __name__ == "__main__":
    unittest.main()