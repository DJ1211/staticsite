import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_one_prop(self):
        node = LeafNode("a", "this is test text", props={"href": "https://www.google.com"})
        self.assertEqual(
            '<a href="https://www.google.com">this is test text</a>' , 
            node.to_html()
        )

    def test_to_html_two_props(self):
        node = LeafNode("a", "this is test text", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(
            '<a href="https://www.google.com" target="_blank">this is test text</a>' , 
            node.to_html()
        )

    def test_to_html_no_prop(self):
        node = LeafNode("p", "this is test text")
        self.assertEqual(
            '<p>this is test text</p>' , 
            node.to_html()
        )

    def test_to_html_special_chars(self):
        node = LeafNode("p!?@", "th*/is i\s| t>es<t¬! text", props={"!#@href": "https://www.go!o*g(l\e.com", "tar£g%et": "_bl?a>n<k"})
        self.assertEqual(
            '<p!?@ !#@href="https://www.go!o*g(l\e.com" tar£g%et="_bl?a>n<k">th*/is i\s| t>es<t¬! text</p!?@>' , 
            node.to_html()
        )

    def test_to_html_no_tag(self):
        node = LeafNode(None, "this is test text")
        self.assertEqual(
            'this is test text' , 
            node.to_html()
        )

    def test_to_html_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_empty_string(self):
        node = LeafNode("p", "")
        self.assertEqual(
            '<p></p>' , 
            node.to_html()
        )

    def test_to_html_white_space(self):
        node = LeafNode("   ", "   ")
        self.assertEqual(
            '<   >   </   >' , 
            node.to_html()
        )

    def test_repr(self):
        node = LeafNode("This is a tag", "This is a leaf node", {"key":"value"})
        self.assertEqual(
            "LeafNode(This is a tag, This is a leaf node, {'key': 'value'})", repr(node)
        )
