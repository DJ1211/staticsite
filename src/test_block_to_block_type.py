import unittest
from textwrap import dedent

from markdown_blocks import block_to_block_type, markdown_to_blocks

class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_block_type_heading(self):
        markdown = """
                # Heading 1
                """
        markdown_blocks = markdown_to_blocks(markdown)
        for block in markdown_blocks:
            block_type = block_to_block_type(block)

        self.assertEqual(block_type, "heading")


    def test_block_to_block_type_code(self):
        markdown = """
                ```
                Code 1
                ```
                """
        markdown_blocks = markdown_to_blocks(markdown)
        for block in markdown_blocks:
            block_type = block_to_block_type(block)

        self.assertEqual(block_type, "code")


    def test_block_to_block_type_quote(self):
        markdown = dedent("""
                > Quote 1
                >> Quote 2
                >> Quote 3
                """).strip()
        markdown_blocks = markdown_to_blocks(markdown)
        for block in markdown_blocks:
            block_type = block_to_block_type(block)

        self.assertEqual(block_type, "quote")


    def test_block_to_block_type_unordered_list(self):
        markdown = dedent("""
                * List 1
                - List 2
                """).strip()
        markdown_blocks = markdown_to_blocks(markdown)
        for block in markdown_blocks:
            block_type = block_to_block_type(block)

        self.assertEqual(block_type, "unordered_list")

    def test_block_to_block_type_ordered_list(self):
        markdown = dedent("""
                1. List 1
                2. List 2
                """).strip()
        markdown_blocks = markdown_to_blocks(markdown)
        for block in markdown_blocks:
            block_type = block_to_block_type(block)

        self.assertEqual(block_type, "ordered_list")

    def test_block_to_block_type_paragraph(self):
        markdown = """
                This is a paragraph
                """
        markdown_blocks = markdown_to_blocks(markdown)
        for block in markdown_blocks:
            block_type = block_to_block_type(block)

        self.assertEqual(block_type, "paragraph")


    def test_block_to_block_type_all(self):
        markdown = dedent("""
                          # Heading 1

                          Paragraph 1
                          
                          ```
                          Code
                          ```
                          
                          > Quote 1
                          >> Quote 2
                          
                          * Unordered List 1
                          - Unordered List 2
                          
                          1. Ordered List 1
                          2. Ordered List 2
                          """)

        
        markdown_blocks = markdown_to_blocks(markdown)
        block_list = []
        expected = ["heading", "paragraph", "code", "quote", "unordered_list", "ordered_list"]
        for block in markdown_blocks:
            block_list.append(block_to_block_type(block))

        self.assertEqual(block_list, expected)

    def test_block_to_block_type_incorrect_markup(self):
        markdown = dedent("""
                          #! Heading 1

                          Paragraph 1
                          
                          ``
                          Code
                          ``
                          
                          !> Quote 1
                          #>> Quote 2
                          
                          .* Unordered List 1
                          '- Unordered List 2
                          
                          3. Ordered List 1
                          21. Ordered List 2
                          """)

        
        markdown_blocks = markdown_to_blocks(markdown)
        block_list = []
        expected = ["paragraph", "paragraph", "paragraph", "paragraph", "paragraph", "paragraph"]
        for block in markdown_blocks:
            block_list.append(block_to_block_type(block))

        self.assertEqual(block_list, expected)
            




if __name__ == "__main__":
    unittest.main()