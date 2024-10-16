from textnode import TextNode

valid_delimeters = ["text", "bold", "italic", "code", "link", "image"]


# old nodes is a list
def split_nodes_delimeter(old_nodes, delimiter, text_type):
    if not delimiter:
        raise Exception("Requires delimeter to be entered")
    if text_type not in valid_delimeters:
        raise Exception("Not a valid text type")
    if not old_nodes:
        raise Exception("Cannot provide an empty node list")
    new_list = []
    count = 0
    for node in old_nodes:
        if node.text_type == "text":
            if delimiter in node.text:
                count += 1
                split_node_text = node.text.split(delimiter)
                for item in split_node_text:
                    if item == split_node_text[1]:
                        new_list.append(TextNode(item, text_type))
                    else:
                        new_list.append(TextNode(item, "text"))
        else:
            new_list.append(node)
    if count == 0:
        raise Exception("invalid markdown syntax")
    return new_list
