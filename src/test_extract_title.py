import unittest
from generate_page import extract_title

class TestExtract_Title(unittest.TestCase):
    def test_extract_title_h1(self):
        text = "# This is a h1 title"
        expected = "This is a h1 title"

        self.assertEqual(extract_title(text), expected)

    def test_extract_title_h2(self):
        text = "## This is a h2 title"
        with self.assertRaises(Exception):
            extract_title(text)

    def test_extract_title_trailing_whitespace(self):
        text = "#      This is a h1 title     "
        expected = "This is a h1 title"

        self.assertEqual(extract_title(text), expected)

    def test_extract_title_multiple_linesh1(self):
        text = "# This is a h1 title\n## This is a h2 title \n\n ### This is a h3 title"
        expected = "This is a h1 title"

        self.assertEqual(extract_title(text), expected)

if __name__ == "__main__":
    unittest.main()