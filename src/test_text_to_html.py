import unittest

from textnode import text_node_to_html_node, TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_text_to_html_node_normal(self):
        text_node = TextNode("Test Text", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)

        self.assertIsNone(html_node.tag)
        self.assertEqual(html_node.value, "Test Text") 
        self.assertIsNone(html_node.props)

    def test_text_to_html_node_bold(self):
        text_node = TextNode("Test Text", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)

        self.assertEqual(html_node.tag, "b") 
        self.assertEqual( html_node.value, "Test Text")
        self.assertIsNone(html_node.props)

    def test_text_to_html_node_italic(self):
        text_node = TextNode("Test Text", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)

        self.assertEqual(html_node.tag, "i") 
        self.assertEqual(html_node.value, "Test Text") 
        self.assertIsNone(html_node.props)

    def test_text_to_html_node_code(self):
        text_node = TextNode("Test Text", TextType.CODE)
        html_node = text_node_to_html_node(text_node)

        self.assertEqual(html_node.tag, "code") 
        self.assertEqual(html_node.value, "Test Text") 
        self.assertIsNone(html_node.props)

    def test_text_to_html_node_link(self):
        text_node = TextNode("Test Text", TextType.LINK, "Test URL")
        html_node = text_node_to_html_node(text_node)

        self.assertEqual(html_node.tag, "a") 
        self.assertEqual(html_node.value, "Test Text") 
        self.assertEqual(html_node.props, {"href":"Test URL"}) 

    def test_text_to_html_node_image(self):
        text_node = TextNode("Test Text", TextType.IMAGE, "Test URL")
        html_node = text_node_to_html_node(text_node)

        self.assertEqual(html_node.tag, "img") 
        self.assertEqual(html_node.value, "") 
        self.assertEqual(html_node.props, {"src":"Test URL", "alt":"Test Text"}) 