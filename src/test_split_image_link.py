import unittest

from split_delimiter import split_nodes_link, split_nodes_image, TextNode, TextType

class TestSplitDelimiter(unittest.TestCase):
    def test_split_image_one_image(self):
        node = TextNode(
                        "This is text with an image ![image](url)",
                        TextType.TEXT,
                        )
        split_node = split_nodes_image([node])
        expected = [
                    TextNode("This is text with an image ", TextType.TEXT),
                    TextNode("image", TextType.IMAGE, "url")
                    ]
        
        self.assertEqual(split_node, expected)

    def test_split_image_two_images(self):
        node = TextNode(
                        "This is text with an image ![image](url) and another image ![image2](url2)",
                        TextType.TEXT,
                        )
        split_node = split_nodes_image([node])
        expected = [
                    TextNode("This is text with an image ", TextType.TEXT),
                    TextNode("image", TextType.IMAGE, "url"),
                    TextNode(" and another image ", TextType.TEXT),
                    TextNode("image2", TextType.IMAGE, "url2")
                    ]
        
        self.assertEqual(split_node, expected)

    def test_split_image_two_images_trailing_text(self):
        node = TextNode(
                        "This is text with an image ![image](url) and another image ![image2](url2) and trailing text",
                        TextType.TEXT,
                        )
        split_node = split_nodes_image([node])
        expected = [
                    TextNode("This is text with an image ", TextType.TEXT),
                    TextNode("image", TextType.IMAGE, "url"),
                    TextNode(" and another image ", TextType.TEXT),
                    TextNode("image2", TextType.IMAGE, "url2"),
                    TextNode(" and trailing text", TextType.TEXT),
                    ]
        
        self.assertEqual(split_node, expected)

    def test_split_image_two_nodes(self):
        node = TextNode(
                        "This is a node with an image ![image](url)",
                        TextType.TEXT,
                        )
        node2 = TextNode(
                        "This is another node with an image ![image2](url2)",
                        TextType.TEXT,
                        )
        split_node = split_nodes_image([node, node2])
        expected = [
                    TextNode("This is a node with an image ", TextType.TEXT),
                    TextNode("image", TextType.IMAGE, "url"),
                    TextNode("This is another node with an image ", TextType.TEXT),
                    TextNode("image2", TextType.IMAGE, "url2")
                    ]
        
        self.assertEqual(split_node, expected)

    def test_split_image_no_links(self):
        node = TextNode(
                        "This is text with no links",
                        TextType.TEXT,
                        )
        split_node = split_nodes_image([node])
        expected = [
                    TextNode("This is text with no links", TextType.TEXT)
                    ]
        
        self.assertEqual(split_node, expected)

    def test_split_image_links_first(self):
        node = TextNode(
                        "![image](url) This is text following an image",
                        TextType.TEXT,
                        )
        split_node = split_nodes_image([node])
        expected = [
                    TextNode("image", TextType.IMAGE, "url"),
                    TextNode(" This is text following an image", TextType.TEXT)
                    ]
        
        self.assertEqual(split_node, expected)

    def test_split_image_special_characters(self):
        node = TextNode(
                        "This is text with an image with special characters ![image](url?@!¬*%~#><,/\|)",
                        TextType.TEXT,
                        )
        split_node = split_nodes_image([node])
        expected = [
                    TextNode("This is text with an image with special characters ", TextType.TEXT),
                    TextNode("image", TextType.IMAGE, "url?@!¬*%~#><,/\|")
                    ]
        
        self.assertEqual(split_node, expected)

    def test_split_image_empty_text(self):
        node = TextNode(
                        "![image](url)",
                        TextType.TEXT,
                        )
        split_node = split_nodes_image([node])
        expected = [
                    TextNode("image", TextType.IMAGE, "url")
                    ]
        
        self.assertEqual(split_node, expected)

    def test_split_link_one_link(self):
        node = TextNode(
                        "This is text with a link [text](url)",
                        TextType.TEXT,
                        )
        split_node = split_nodes_link([node])
        expected = [
                    TextNode("This is text with a link ", TextType.TEXT),
                    TextNode("text", TextType.LINK, "url")
                    ]
        
        self.assertEqual(split_node, expected)

    def test_split_link_two_links(self):
        node = TextNode(
                        "This is text with a link [text](url) and another link [text2](url2)",
                        TextType.TEXT,
                        )
        split_node = split_nodes_link([node])
        expected = [
                    TextNode("This is text with a link ", TextType.TEXT),
                    TextNode("text", TextType.LINK, "url"),
                    TextNode(" and another link ", TextType.TEXT),
                    TextNode("text2", TextType.LINK, "url2")
                    ]
        
        self.assertEqual(split_node, expected)

    def test_split_link_two_links_trailing_text(self):
        node = TextNode(
                        "This is text with a link [text](url) and another link [text2](url2) and trailing text",
                        TextType.TEXT,
                        )
        split_node = split_nodes_link([node])
        expected = [
                    TextNode("This is text with a link ", TextType.TEXT),
                    TextNode("text", TextType.LINK, "url"),
                    TextNode(" and another link ", TextType.TEXT),
                    TextNode("text2", TextType.LINK, "url2"),
                    TextNode(" and trailing text", TextType.TEXT),
                    ]
        
        self.assertEqual(split_node, expected)

    def test_split_link_two_nodes(self):
        node = TextNode(
                        "This is text with a node [text](url)",
                        TextType.TEXT,
                        )
        node2 = TextNode(
                        "This is text with another node [text2](url2)",
                        TextType.TEXT,
                        )
        split_node = split_nodes_link([node, node2])
        expected = [
                    TextNode("This is text with a node ", TextType.TEXT),
                    TextNode("text", TextType.LINK, "url"),
                    TextNode("This is text with another node ", TextType.TEXT),
                    TextNode("text2", TextType.LINK, "url2")
                    ]
        
        self.assertEqual(split_node, expected)

    def test_split_link_no_links(self):
        node = TextNode(
                        "This is text with no links",
                        TextType.TEXT,
                        )
        split_node = split_nodes_link([node])
        expected = [
                    TextNode("This is text with no links", TextType.TEXT)
                    ]
        
        self.assertEqual(split_node, expected)

    def test_split_link_links_first(self):
        node = TextNode(
                        "[text](url) This is text following a link",
                        TextType.TEXT,
                        )
        split_node = split_nodes_link([node])
        expected = [
                    TextNode("text", TextType.LINK, "url"),
                    TextNode(" This is text following a link", TextType.TEXT)
                    ]
        
        self.assertEqual(split_node, expected)

    def test_split_link_special_characters(self):
        node = TextNode(
                        "This is text with a link with special characters [text](url?@!¬*%~#><,/\|)",
                        TextType.TEXT,
                        )
        split_node = split_nodes_link([node])
        expected = [
                    TextNode("This is text with a link with special characters ", TextType.TEXT),
                    TextNode("text", TextType.LINK, "url?@!¬*%~#><,/\|")
                    ]
        
        self.assertEqual(split_node, expected)

    def test_split_link_empty_text(self):
        node = TextNode(
                        "[text](url)",
                        TextType.TEXT,
                        )
        split_node = split_nodes_link([node])
        expected = [
                    TextNode("text", TextType.LINK, "url")
                    ]
        
        self.assertEqual(split_node, expected)

    def test_split_link_empty_link(self):
        node = TextNode(
                        "This is text with an empty link [](url)",
                        TextType.TEXT,
                        )
        split_node = split_nodes_link([node])
        expected = [
                    TextNode("This is text with an empty link ", TextType.TEXT),
                    TextNode("", TextType.LINK, "url")
                    ]
        
        self.assertEqual(split_node, expected)

    def test_split_link_empty_url(self):
        node = TextNode(
                        "This is text with an empty link [text]()",
                        TextType.TEXT,
                        )
        split_node = split_nodes_link([node])
        expected = [
                    TextNode("This is text with an empty link ", TextType.TEXT),
                    TextNode("text", TextType.LINK, "")
                    ]
        
        self.assertEqual(split_node, expected)

    def test_split_link_multiple_links(self):
        node = TextNode(
                        "This is text with multiple links [text](url)[text2](url2)",
                        TextType.TEXT,
                        )
        split_node = split_nodes_link([node])
        expected = [
                    TextNode("This is text with multiple links ", TextType.TEXT),
                    TextNode("text", TextType.LINK, "url"),
                    TextNode("text2", TextType.LINK, "url2")
                    ]
        
        self.assertEqual(split_node, expected)

if __name__ == "__main__":
    unittest.main()