import unittest
from textwrap import dedent

from markdown_blocks import markdown_to_blocks

class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks_one_line(self):
        markdown = "# This is a heading"
        output = markdown_to_blocks(markdown)
        expected = ["# This is a heading"]

        self.assertEqual(output, expected)

    def test_markdown_to_blocks_two_lines(self):
        markdown = dedent("""Line 1
        
        Line 2""".strip())

        output = markdown_to_blocks(markdown)
        expected = ["Line 1", "Line 2"]

        self.assertEqual(output, expected)

    def test_markdown_to_blocks_three_lines(self):
        markdown = dedent("""
        Line 1
        
        Line 2
                          
        Line 3
        """).strip()

        output = markdown_to_blocks(markdown)
        expected = ["Line 1", "Line 2", "Line 3"]

        self.assertEqual(output, expected)

    def test_markdown_to_blocks_list_items(self):
        markdown = dedent("""
        Line 1
        
        Line 2
                          
        List 1
        List 2
        List 3
        """).strip()

        output = markdown_to_blocks(markdown)
        expected = ["Line 1", "Line 2", "List 1\nList 2\nList 3"]

        self.assertEqual(output, expected)

    def test_markdown_to_blocks_multiple_list_items(self):
        markdown = dedent("""
        Line 1
        
        Line 2
                          
        List 1
        List 2
        List 3
                          
        List2 1
        List2 2
        List2 3
        """).strip()

        output = markdown_to_blocks(markdown)
        expected = ["Line 1", "Line 2", "List 1\nList 2\nList 3", "List2 1\nList2 2\nList2 3"]

        self.assertEqual(output, expected)

    def test_markdown_to_blocks_markdown_elementss(self):
        markdown = dedent("""
        # Line 1
        
        **Line 2**
                          
        *List 1*
        `List 2`
        List 3
        """).strip()

        output = markdown_to_blocks(markdown)
        expected = ["# Line 1", "**Line 2**", "*List 1*\n`List 2`\nList 3"]

        self.assertEqual(output, expected)


    def test_markdown_to_blocks_odd_abundant_newline(self):
        markdown = dedent("""
        Line 1
        
                          
        Line 2
                          
        List 1
        List 2
        List 3
        """).strip()

        output = markdown_to_blocks(markdown)
        expected = ["Line 1", "Line 2", "List 1\nList 2\nList 3"]

        self.assertEqual(output, expected)

    def test_markdown_to_blocks_even_abundant_newline(self):
        markdown = dedent("""
        Line 1
        
                          
                          
        Line 2
                          
        List 1
        List 2
        List 3
        """).strip()

        output = markdown_to_blocks(markdown)
        expected = ["Line 1", "Line 2", "List 1\nList 2\nList 3"]

        self.assertEqual(output, expected)

    def test_markdown_to_blocks_with_whitespace(self):
        markdown = dedent("""
        Line 1    
        
           Line 2     
        
        List 1  
          List 2
        List 3   
        """).strip()

        output = markdown_to_blocks(markdown)
        expected = ["Line 1", "Line 2", "List 1  \n  List 2\nList 3"]

        self.assertEqual(output, expected)

if __name__ == "__main__":
    unittest.main()