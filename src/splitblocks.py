from inline import text_to_textnodes
from leafnode import LeafNode
from parentnode import ParentNode

def markdown_to_blocks(markdown):
    if not markdown:
        raise Exception("No Markdown Text Provided")
    final = []
    for block in markdown.split("\n\n"):
        if block.strip():
            final.append(block.strip())
    return final

# Heading needs to start with a # and be proceeded by a space. However, the heading can be up to 6 hashes followed by a space instead of just one hash only.
def is_heading(list_of_markdown):
    if list_of_markdown[0][0] == "#":
        for line in list_of_markdown:
            count = 0
            for char in line:
                if char == "#":
                    count += 1
                elif count == 7:
                    return False
                elif char == " " and 1<= count <=6:
                    break
                else:
                    return False
        return True
    else:
        return False
    
def is_code(list_of_markdown):
    if list_of_markdown[0][0:3] == "```":
        for line in list_of_markdown:
            if line[0:3] != "```" or line[-3:] != "```":
                return False
        return True
    
def is_quote(list_of_markdown):
    if list_of_markdown[0][0] == ">":
        for line in list_of_markdown:
            if line[0] != ">":
                return False
        return True
    
def is_unordered_list(list_of_markdown):
    if list_of_markdown[0][0:2] == "* " or list_of_markdown[0][0:2] == "- ":
        for line in list_of_markdown:
            if line[0:2] != "* ":
                if line[0:2] != "- ":
                    return False
        return True
def is_orderedlist(list_of_markdown):
    if list_of_markdown[0][0].isdigit():
        for line in list_of_markdown:
            count = 0
            for char in line:
                if not char.isdigit():
                    if char == ".":
                        if line[count + 1] != " ":
                            return False
                        else:
                            break
                    else:
                        return False
                else:
                    count += 1
        return True
    
def block_to_block_type(block_of_markdown):
    if not block_of_markdown:
        raise Exception("No markdown provided!")
    if len(block_of_markdown) == 1:
        return "paragraph"
    split = block_of_markdown.split("\n")
    if is_heading(split):
        return "heading"
    if is_code(split):
        return "code"
    if is_quote(split):
        return "quote"
    if is_unordered_list(split):
        return "unordered list"
    if is_orderedlist(split):
        return "ordered list"
    # Didn't find supported type so default to paragraph
    else:
        return "paragraph"

def heading_block_to_html_node(block):
    lines = block.split("\n")
    new_list = []
    for line in lines:
        count = 0
        for char in line:
            if "#" == char:
                count += 1
            else:
                break
        if len(text_to_textnodes(line)) > 1:
            new_list.append(ParentNode(f"h{count}", text_to_textnodes(line.lstrip("# "))))
        else:
            new_list.append(LeafNode(f"h{count}", line.lstrip("# ")))
    return new_list

def markdown_to_html(markdown):
    pass
    # split into blocks using markdown to blocks function
    blocks = markdown_to_blocks(markdown)
    # lopo through the returned list of blocks and determine wwhat type the block is with block to block type function
    for block in blocks:
        type_of_block = block_to_block_type(block)
    # once you know what type of block you are in, convert that block to an htmlnode. assign the proper children to that block (use an additional function to help with this)

    # make sure all blocks looped through then go under a single parent htmlnode which should just be a div and then return it.
    # return one html node that then contains the tree of html nodes

test = """
#### This is a heading

1. With a list
2. inside of it.
3. oh no!

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""
print(markdown_to_blocks(test))
ex = markdown_to_blocks(test)
first_block = ex[0]
print(first_block)
print(heading_block_to_html(first_block)[0])