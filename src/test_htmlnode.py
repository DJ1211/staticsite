import unittest

from htmlnode import HTMLNode

    
class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_one_prop(self):
        node = HTMLNode(props={"href": "https://www.google.com"})
        self.assertEqual(
            ' href="https://www.google.com"' , 
            node.props_to_html()
        )

    def test_props_to_html_two_props(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(
            ' href="https://www.google.com" target="_blank"' ,
            node.props_to_html()
        )

    def test_props_to_html_none_prop(self):
        node = HTMLNode(props=None)
        self.assertEqual(
            "",
            node.props_to_html()
        )

    def test_props_to_html_special_props(self):
        node = HTMLNode(props={"!#@href": "https://www.go!o*g(l\e.com", "tar£g%et": "_bl?a>n<k"})
        self.assertEqual(
            ' !#@href="https://www.go!o*g(l\e.com" tar£g%et="_bl?a>n<k"' ,
            node.props_to_html()
        )



if __name__ == "__main__":
    unittest.main()