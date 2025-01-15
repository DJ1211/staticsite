import unittest

from split_delimiter import extract_markdown_images, extract_markdown_links

class TestTextNode(unittest.TestCase):
    def test_extract_markdown_images_one_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        expected = [('rick roll', 'https://i.imgur.com/aKaOqIh.gif')]

        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_markdown_images_two_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected = [('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')]

        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_markdown_images_incorrect_markdown(self):
        text = "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected = [('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')]

        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_markdown_images_with_links(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and and [to youtube](https://www.youtube.com/@bootdotdev)"
        expected = [('rick roll', 'https://i.imgur.com/aKaOqIh.gif')]

        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_markdown_links_one_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev)"
        expected = [('to boot dev', 'https://www.boot.dev')]

        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_markdown_links_two_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        expected = [('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')]

        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_markdown_links_incorrect_markdown(self):
        text = "This is text with a link ![to boot dev](https://www.boot.dev)"
        expected = []

        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_markdown_links_with_image(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected = [('to boot dev', 'https://www.boot.dev')]

        self.assertEqual(extract_markdown_links(text), expected)

if __name__ == "__main__":
    unittest.main()