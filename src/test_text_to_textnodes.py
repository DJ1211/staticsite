import unittest

from split_delimiter import text_to_textnodes, TextNode, TextType

class TestTextToTextNode(unittest.TestCase):
    def test_textnodes_bold(self):
        text = "This is **text**"
        text_nodes = text_to_textnodes(text)
        expected = [
                    TextNode("This is ", TextType.TEXT),
                    TextNode("text", TextType.BOLD)
                    ]
        
        self.assertEqual(text_nodes, expected)

    def test_textnodes_italic(self):
        text = "This is *italic*"
        text_nodes = text_to_textnodes(text)
        expected = [
                    TextNode("This is ", TextType.TEXT),
                    TextNode("italic", TextType.ITALIC)
                    ]
        
        self.assertEqual(text_nodes, expected)

    def test_textnodes_code(self):
        text = "This is `code`"
        text_nodes = text_to_textnodes(text)
        expected = [
                    TextNode("This is ", TextType.TEXT),
                    TextNode("code", TextType.CODE)
                    ]
        
        self.assertEqual(text_nodes, expected)

    def test_textnodes_image(self):
        text = "This is an image ![image](url)"
        text_nodes = text_to_textnodes(text)
        expected = [
                    TextNode("This is an image ", TextType.TEXT),
                    TextNode("image", TextType.IMAGE, "url"),
                    ]
        
        self.assertEqual(text_nodes, expected)

    def test_textnodes_link(self):
        text = "This is a link [text](url)"
        text_nodes = text_to_textnodes(text)
        expected = [
                    TextNode("This is a link ", TextType.TEXT),
                    TextNode("text", TextType.LINK, "url"),
                    ]
        
        self.assertEqual(text_nodes, expected)

    def test_textnodes_plain_text(self):
        text = "This is plain text"
        text_nodes = text_to_textnodes(text)
        expected = [
                    TextNode("This is plain text", TextType.TEXT),
                    ]
        
        self.assertEqual(text_nodes, expected)

    def test_textnodes_all(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        text_nodes = text_to_textnodes(text)
        expected = [
                    TextNode("This is ", TextType.TEXT),
                    TextNode("text", TextType.BOLD),
                    TextNode(" with an ", TextType.TEXT),
                    TextNode("italic", TextType.ITALIC),
                    TextNode(" word and a ", TextType.TEXT),
                    TextNode("code block", TextType.CODE),
                    TextNode(" and an ", TextType.TEXT),
                    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                    TextNode(" and a ", TextType.TEXT),
                    TextNode("link", TextType.LINK, "https://boot.dev")
                    ]
        
        self.assertEqual(text_nodes, expected)

    def test_textnodes_multiple_bold(self):
        text = "This is **text** and more **text**"
        text_nodes = text_to_textnodes(text)
        expected = [
                    TextNode("This is ", TextType.TEXT),
                    TextNode("text", TextType.BOLD),
                    TextNode(" and more ", TextType.TEXT),
                    TextNode("text", TextType.BOLD)
                    ]
        
        self.assertEqual(text_nodes, expected)

    def test_textnodes_incorrect_markdown(self):
        text = "This is <text>"
        text_nodes = text_to_textnodes(text)
        expected = [
                    TextNode("This is <text>", TextType.TEXT)
                    ]
        
        self.assertEqual(text_nodes, expected)


if __name__ == "__main__":
    unittest.main()