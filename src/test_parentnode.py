import unittest

from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_no_child(self):
        node = ParentNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()
        
    def test_to_html_one_child(self):
        node = ParentNode("p", 
                            [
                            LeafNode("b", "Bold")
                            ]
                          )
        self.assertEqual(
            '<p><b>Bold</b></p>' , 
            node.to_html()
        )

    def test_to_html_two_child(self):
        node = ParentNode("p",
                            [ 
                            LeafNode("b", "Bold"),
                            LeafNode("i", "Italic")
                            ] 
                          )
        self.assertEqual(
            '<p><b>Bold</b><i>Italic</i></p>' , 
            node.to_html()
        )

    def test_to_html_child_no_value(self):
        node = ParentNode("p",
                            [ 
                            LeafNode("b", None),
                            LeafNode("i", "Italic")
                            ] 
                          )
        with self.assertRaises(ValueError):
            node.to_html()


    def test_to_html_nested_parent(self):
        nested_node = ParentNode("div",
                                    [
                                    LeafNode("b", "Bold"),
                                    LeafNode(None, "Normal"),
                                    ParentNode("p", [
                                                    LeafNode("i", "Italic")
                                                    ])
                                    ]
                                )
        self.assertEqual(
            '<div><b>Bold</b>Normal<p><i>Italic</i></p></div>' , 
            nested_node.to_html()
        )

    def test_to_html_parent_prop(self):
        edge_case = ParentNode("div",
                                    [
                                    ParentNode("p", [
                                                    LeafNode(None, "Text1"),
                                                    ParentNode("span", [
                                                                        LeafNode("b", "Bold")
                                                                        ]),
                                                    LeafNode(None, "Text2")
                                                    ]),
                                    LeafNode(None, "Text3")
                                    ],
                                {"class": "wrapper"}
                                )
        self.assertEqual(
            '<div class="wrapper"><p>Text1<span><b>Bold</b></span>Text2</p>Text3</div>' , 
            edge_case.to_html()
        )

    def test_to_html_special_characters(self):
        node = ParentNode("p!@#", 
                            [
                            LeafNode("b/<>", "B!?~old")
                            ]
                          )
        self.assertEqual(
            '<p!@#><b/<>>B!?~old</b/<>></p!@#>' , 
            node.to_html()
        )
        
    def test_empty_children_list(self):
        node = ParentNode("p", [])
        self.assertEqual("<p></p>", node.to_html())

    def test_no_tag(self):
        node = ParentNode(None, [LeafNode("b", "Bold")])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_repr(self):
        node = ParentNode("This is a tag", "This is a child", {"key":"value"})
        self.assertEqual(
            "ParentNode(This is a tag, This is a child, {'key': 'value'})", repr(node)
        )

if __name__ == "__main__":
    unittest.main()