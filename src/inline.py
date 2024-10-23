from textnode import TextNode
from functools import reduce
import re

valid_delimeters = ["text", "bold", "italic", "code", "link", "image"]


def split_nodes_delimeter(old_nodes, delimiter, text_type):
    if not delimiter:
        raise Exception("Requires delimeter to be entered")
    if text_type not in valid_delimeters:
        raise Exception("Not a valid text type")
    if not old_nodes:
        raise Exception("Cannot provide an empty node list")
    new_list = []
    # count used to determine if delim found in string for later error handling.
    count = 0
    for node in old_nodes:
        if node.text_type != "text":
            new_list.append(node)
            continue

        buffer = ""
        buffer2 = ""
        delim_count = 0
        inside_delimeter = False
        i = 0

        while i < len(node.text):
            if node.text[i: i + len(delimiter)] == delimiter:
                if delimiter == "*":
                    if i + 1 < len(node.text) and node.text[i + 1] == "*":
                        # This means we're dealing with "**" (bold), so we skip it
                        buffer += "**"  # Add the double asterisks to the buffer as plain text
                        i += 2  # Skip both asterisks
                        continue  # Move to the next iteration
                if buffer and not inside_delimeter:
                    buffer2 = buffer
                    buffer = ""
                inside_delimeter = True
                delim_count += 1
                if delim_count == 2:
                    if delimiter ==  "*" and i + 1 < len(node.text) and node.text[i + 1] == "*":
                        delim_count -= 1
                        i += 1
                    else:
                        if buffer2:
                            new_list.append(TextNode(buffer2, "text"))
                        new_list.append(TextNode(buffer, text_type))
                        buffer = ""
                        delim_count = 0
                        inside_delimeter = False
                        # delimeter was in string.
                        count += 1
                i += len(delimiter)
            else:
                buffer += node.text[i]
                i += 1
        if delim_count == 1:
            new_list.append(TextNode(buffer2 + buffer, "text"))
        else:
            if buffer:
                new_list.append(TextNode(buffer, "text"))
    if count == 0:
        return old_nodes
    return new_list


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_images(old_nodes):
    if not old_nodes:
        raise Exception("Cannot provide an empty node list")
    list = []
    for node in old_nodes:
        # check if node is empty
        if not node:
            continue
        #check if node is a 'text' text-type
        if node.text_type != "text":
            list.append(node)
            continue

        images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", node.text)

        #check if images found in text
        if not images:
            list.append(node)
            continue

        remaining_text = node.text
        i = 0
        while i < 1:
            for image in images:
                split = remaining_text.split(f"![{image[0]}]({image[1]})", 1)
                if len(split) > 1:
                    alt_text = image[0]
                    url = image[1]
                    list.append(TextNode(split[0], "text"))
                    list.append(TextNode(alt_text, "image", url))
                    remaining_text = split[1]
                else:
                    if split[0]:
                        list.append(TextNode(split[0], "text"))
                    i += 1
    if not list:
        return old_nodes
    return list

def split_nodes_links(old_nodes):
    if not old_nodes:
        raise Exception("Cannot provide an empty node list")
    list = []
    for node in old_nodes:
         # check if node is empty
        if not node:
            continue

        # check if node is a 'text' text-type
        if node.text_type != "text":
            list.append(node)
            continue

        links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", node.text)

        #check if links found in text
        if not links:
            list.append(node)
            continue

        remaining_text = node.text
        i = 0
        while i < 1:
            for link in links:
                split = remaining_text.split(f"[{link[0]}]({link[1]})", 1)
                if len(split) > 1:
                    alt_text = link[0]
                    url = link[1]
                    list.append(TextNode(split[0], "text"))
                    list.append(TextNode(alt_text, "link", url))
                    remaining_text = split[1]
                else:
                    if split[0]:
                        list.append(TextNode(split[0], "text"))
                i += 1
    if not list:
        return old_nodes
    return list


def text_to_textnodes(text):
    if not text:
        raise Exception("No text provided to convert")
    textnode_list = [TextNode(text, "text")]
    return split_nodes_links(split_nodes_images(split_nodes_delimeter(split_nodes_delimeter(split_nodes_delimeter(textnode_list, "**", "bold"), "*", "italic"), "`", "code")))