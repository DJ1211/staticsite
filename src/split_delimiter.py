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
            if i % 2 == 0:
                new_nodes.append(TextNode(text, TextType.TEXT))
            else:
                new_nodes.append(TextNode(text, text_type))
        
        if len(split_node) % 2 != 1:
             raise Exception("Unmatched delimiter")
        
        final_nodes.extend(new_nodes)

    return final_nodes

