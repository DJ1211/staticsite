import unittest

from split_delimiter import split_nodes_delimiter, TextNode, TextType

class TestSplitDelimiter(unittest.TestCase):
    def test_split_delimiter_one_node_bold(self):
        text_node = TextNode("This is **bold** test text", TextType.TEXT)
        delimit_node = split_nodes_delimiter([text_node], "**", TextType.BOLD)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" test text", TextType.TEXT),
        ]

        self.assertEqual(delimit_node, expected)

    def test_split_delimiter_one_node_italic(self):
        text_node = TextNode("This is *italic* test text", TextType.TEXT)
        delimit_node = split_nodes_delimiter([text_node], "*", TextType.ITALIC)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" test text", TextType.TEXT),
        ]

        self.assertEqual(delimit_node, expected)

    def test_split_delimiter_one_node_code(self):
        text_node = TextNode("This is `code` test text", TextType.TEXT)
        delimit_node = split_nodes_delimiter([text_node], "`", TextType.CODE)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" test text", TextType.TEXT),
        ]

        self.assertEqual(delimit_node, expected)

    def test_split_delimiter_one_not_text(self):
        text_node = TextNode("This is **bold** test text", TextType.BOLD)
        delimit_node = split_nodes_delimiter([text_node], "**", TextType.BOLD)
        expected = [TextNode("This is **bold** test text", TextType.BOLD)]

        self.assertEqual(delimit_node, expected)

    def test_split_delimiter_one_no_delimiter(self):
        text_node = TextNode("This is **bold** test text", TextType.TEXT)

        with self.assertRaises(Exception) as context:
            split_nodes_delimiter([text_node], None, TextType.BOLD)
        
        self.assertEqual(str(context.exception), "Missing delimiter")

    def test_split_delimiter_one_unmatched_delimiter(self):
        text_node = TextNode("This is **bold** **test text", TextType.TEXT)

        with self.assertRaises(Exception) as context:
            split_nodes_delimiter([text_node], "**", TextType.BOLD)
        
        self.assertEqual(str(context.exception), "Unmatched delimiter")