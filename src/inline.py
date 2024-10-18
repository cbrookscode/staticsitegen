from textnode import TextNode

import re

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



def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_images(old_nodes):
    if text_type not in valid_delimeters:
        raise Exception("Not a valid text type")
    if not old_nodes:
        raise Exception("Cannot provide an empty node list")
    list = []
    for node in old_nodes:
        images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", node.text)
        remaining_text = node.text
        for image in images:
            split = remaining_text.split(f"[{image[0]}]({image[1]})", 1)
            alt_text = image[0]
            url = image[1]
            list.append(TextNode(split[0][:-1], "text"))
            list.append(TextNode(alt_text, "image", url))
            remaining_text = split[1]
    return list

def split_nodes_links(old_nodes):
    list = []
    for node in old_nodes:
        links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", node.text)
        remaining_text = node.text
        for link in links:
            split = remaining_text.split(f"[{link[0]}]({link[1]})", 1)
            alt_text = link[0]
            url = link[1]
            list.append(TextNode(split[0], "text"))
            list.append(TextNode(alt_text, "link", url))
            remaining_text = split[1]
    return list