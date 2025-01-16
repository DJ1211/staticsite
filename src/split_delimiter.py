import re

from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    final_nodes = []
    if delimiter is None:
        raise Exception("Missing delimiter")
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            final_nodes.append(node)
            continue

        split_node = node.text.split(delimiter)
        new_nodes = []

        for i, text in enumerate(split_node):
            if text != "":
                if i % 2 == 0:
                    new_nodes.append(TextNode(text, TextType.TEXT))
                else:
                    new_nodes.append(TextNode(text, text_type))
        
        if len(split_node) % 2 != 1:
             raise Exception("Unmatched delimiter")
        
        final_nodes.extend(new_nodes)

    return final_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def split_nodes_image(old_nodes):
    
    final_nodes = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            final_nodes.append(node)
            continue

        extracted_text = extract_markdown_images(node.text)
        split_nodes = []

        if not extracted_text:
            final_nodes.append(node)
            continue
        
        for i, (image_alt, image_link) in enumerate(extracted_text):
                sections = node.text.split(f"![{image_alt}]({image_link})", 1)
                if len(sections) != 2:
                    raise ValueError("Invalid markdown, image section not closed")
                if sections[0] != "":
                    split_nodes.append(TextNode(sections[0], TextType.TEXT))
                split_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
                
                node.text = sections[1]

        if sections[1] != "":
            split_nodes.append(TextNode(sections[1], TextType.TEXT))

        final_nodes.extend(split_nodes)

    return final_nodes


def split_nodes_link(old_nodes):
    
    final_nodes = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            final_nodes.append(node)
            continue


        extracted_text = extract_markdown_links(node.text)
        split_nodes = []

        if not extracted_text:
            final_nodes.append(node)
            continue
        
        for i, (link_text, link_url) in enumerate(extracted_text):
                sections = node.text.split(f"[{link_text}]({link_url})", 1)
                if len(sections) != 2:
                    raise ValueError("Invalid markdown, image section not closed")
                if sections[0] != "":
                    split_nodes.append(TextNode(sections[0], TextType.TEXT))
                split_nodes.append(TextNode(link_text, TextType.LINK, link_url))
                
                node.text = sections[1]

        if sections[1] != "":
            split_nodes.append(TextNode(sections[1], TextType.TEXT))

        final_nodes.extend(split_nodes)

    return final_nodes

def text_to_textnodes(text):

    starting_node = TextNode(text, TextType.TEXT)
    nodes = [starting_node]
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

    return nodes