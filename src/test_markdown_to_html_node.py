import unittest

from markdown_blocks import markdown_to_html_node

class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_markdown_to_html_block_one_heading(self):
        markdown = """# This is a heading"""
        node = markdown_to_html_node(markdown)
        html_node = node.to_html()
        expected = "<div><h1>This is a heading</h1></div>"

        self.assertEqual(html_node, expected)
    
    def test_markdown_to_html_block_two_headings(self):
        markdown = """# This is a heading\n\n## This is a 2nd heading"""
        node = markdown_to_html_node(markdown)
        html_node = node.to_html()
        expected = "<div><h1>This is a heading</h1><h2>This is a 2nd heading</h2></div>"

        self.assertEqual(html_node, expected)

    def test_markdown_to_html_block_three_headings(self):
        markdown = """# This is a heading\n\n## This is a 2nd heading\n\n### This is a 3rd heading"""
        node = markdown_to_html_node(markdown)
        html_node = node.to_html()
        expected = "<div><h1>This is a heading</h1><h2>This is a 2nd heading</h2><h3>This is a 3rd heading</h3></div>"

        self.assertEqual(html_node, expected)

    def test_markdown_to_html_block_four_headings(self):
        markdown = """# This is a heading\n\n## This is a 2nd heading\n\n### This is a 3rd heading\n\n#### This is a 4th heading"""
        node = markdown_to_html_node(markdown)
        html_node = node.to_html()
        expected = "<div><h1>This is a heading</h1><h2>This is a 2nd heading</h2><h3>This is a 3rd heading</h3><h4>This is a 4th heading</h4></div>"

        self.assertEqual(html_node, expected)

    def test_markdown_to_html_block_five_headings(self):
        markdown = """# This is a heading\n\n## This is a 2nd heading\n\n### This is a 3rd heading\n\n#### This is a 4th heading\n\n##### This is a 5th heading"""
        node = markdown_to_html_node(markdown)
        html_node = node.to_html()
        expected = "<div><h1>This is a heading</h1><h2>This is a 2nd heading</h2><h3>This is a 3rd heading</h3><h4>This is a 4th heading</h4><h5>This is a 5th heading</h5></div>"

        self.assertEqual(html_node, expected)

    def test_markdown_to_html_block_six_headings(self):
        markdown = """# This is a heading\n\n## This is a 2nd heading\n\n### This is a 3rd heading\n\n#### This is a 4th heading\n\n##### This is a 5th heading\n\n###### This is a 6th heading"""
        node = markdown_to_html_node(markdown)
        html_node = node.to_html()
        expected = "<div><h1>This is a heading</h1><h2>This is a 2nd heading</h2><h3>This is a 3rd heading</h3><h4>This is a 4th heading</h4><h5>This is a 5th heading</h5><h6>This is a 6th heading</h6></div>"

        self.assertEqual(html_node, expected)

    def test_markdown_to_html_block_code_block(self):
        markdown = """```This is a code block```"""
        node = markdown_to_html_node(markdown)
        html_node = node.to_html()
        expected = "<div><pre><code>This is a code block</code></pre></div>"

        self.assertEqual(html_node, expected)

    def test_markdown_to_html_block_quote(self):
        markdown = """> This is a quote"""
        node = markdown_to_html_node(markdown)
        html_node = node.to_html()
        expected = "<div><blockquote>This is a quote</blockquote></div>"

        self.assertEqual(html_node, expected)

    def test_markdown_to_html_block_multiple_quotes(self):
        markdown = """> This is a quote\n>This is a 2nd quote"""
        node = markdown_to_html_node(markdown)
        html_node = node.to_html()
        expected = "<div><blockquote>This is a quote\nThis is a 2nd quote</blockquote></div>"

        self.assertEqual(html_node, expected)

    def test_markdown_to_html_block_unordered_list(self):
        markdown = """* List Item 1\n- List Item 2"""
        node = markdown_to_html_node(markdown)
        html_node = node.to_html()
        expected = "<div><ul><li>List Item 1</li><li>List Item 2</li></ul></div>"

        self.assertEqual(html_node, expected)

    def test_markdown_to_html_block_ordered_list(self):
        markdown = """1. List Item 1\n2. List Item 2"""
        node = markdown_to_html_node(markdown)
        html_node = node.to_html()
        expected = "<div><ol><li>List Item 1</li><li>List Item 2</li></ol></div>"

        self.assertEqual(html_node, expected)

    def test_markdown_to_html_block_paragraph(self):
        markdown = """This is a paragraph with **bold** text and *italic* text and `code` text and an image ![image](url) and a link [text](url)"""
        node = markdown_to_html_node(markdown)
        html_node = node.to_html()
        expected = '<div><p>This is a paragraph with <b>bold</b> text and <i>italic</i> text and <code>code</code> text and an image <img src="url" alt="image"></img> and a link <a href="url">text</a></p></div>'

        self.maxDiff = None
        self.assertEqual(html_node, expected)

    def test_markdown_to_html_block_all(self):
        markdown = """# This is a heading\n\n```This is a code block```\n\n> This is a quote\n\n* Unordered List Item 1\n\n1. Ordered List Item 1\n\nThis is a paragraph with **bold** text and *italic* text and `code` text and an image ![image](url) and a link [text](url)"""
        node = markdown_to_html_node(markdown)
        html_node = node.to_html()
        expected = '<div><h1>This is a heading</h1><pre><code>This is a code block</code></pre><blockquote>This is a quote</blockquote><ul><li>Unordered List Item 1</li></ul><ol><li>Ordered List Item 1</li></ol><p>This is a paragraph with <b>bold</b> text and <i>italic</i> text and <code>code</code> text and an image <img src="url" alt="image"></img> and a link <a href="url">text</a></p></div>'

        self.maxDiff = None
        self.assertEqual(html_node, expected)

    def test_markdown_to_html_block_heading_with_bold_text(self):
        markdown = """# This is a heading **with bold text**"""
        node = markdown_to_html_node(markdown)
        html_node = node.to_html()
        expected = "<div><h1>This is a heading <b>with bold text</b></h1></div>"

        self.assertEqual(html_node, expected)

    def test_markdown_to_html_block_heading_incorrect_markdown(self):
        markdown = """! This is a heading"""
        node = markdown_to_html_node(markdown)
        html_node = node.to_html()
        expected = "<div><p>! This is a heading</p></div>"

        self.assertEqual(html_node, expected)

        


if __name__ == "__main__":
    unittest.main()