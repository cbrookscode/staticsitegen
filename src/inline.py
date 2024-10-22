from textnode import TextNode

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
        delim_count = 0
        inside_delimeter = False
        i = 0
        while i < len(node.text):
            if node.text[i: i + len(delimiter)] == delimiter:
                if buffer and not inside_delimeter:
                    new_list.append(TextNode(buffer, "text"))
                    buffer = ""
                inside_delimeter = True
                delim_count += 1
                if delim_count == 2:
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
        new_list.append(TextNode(buffer, "text"))
    if count == 0:
        raise Exception("invalid markdown syntax")
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
        for image in images:
            split = remaining_text.split(f"![{image[0]}]({image[1]})", 1)
            alt_text = image[0]
            url = image[1]
            list.append(TextNode(split[0], "text"))
            list.append(TextNode(alt_text, "image", url))

            #update variable to only include remainder of text left
            remaining_text = split[1]
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
        for link in links:
            split = remaining_text.split(f"[{link[0]}]({link[1]})", 1)
            alt_text = link[0]
            url = link[1]
            list.append(TextNode(split[0], "text"))
            list.append(TextNode(alt_text, "link", url))
            remaining_text = split[1]
    if not list:
        return old_nodes
    return list


Markdown_text = "This is **text** with an *italic* word **and** a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

# valid_delimeters = ["text", "bold", "italic", "code", "link", "image"]
def text_to_textnodes(text):
    textnode_list = [TextNode(text, "text")]
    textnode_list = split_nodes_delimeter(textnode_list, "**", "bold")
    textnode_list = split_nodes_delimeter(textnode_list, "*", "italic")
    textnode_list = split_nodes_delimeter(textnode_list, "`", "code")
    textnode_list = split_nodes_images(textnode_list)
    textnode_list = split_nodes_links(textnode_list)
    return textnode_list

print(text_to_textnodes(Markdown_text))
