from inline import text_to_textnodes
from leafnode import LeafNode
from parentnode import ParentNode
from textnode import TextNode

def markdown_to_blocks(markdown):
    if not markdown:
        raise Exception("No Markdown Text Provided")
    final = []
    for block in markdown.split("\n\n"):
        if block.strip():
                final.append(block.strip())
    return final

# Heading needs to start with a # and be proceeded by a space. However, the heading can be up to 6 hashes followed by a space instead of just one hash only.
def is_heading(line):
    if len(line) <= 1:
        return False
    if line[0] == "#":
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
    
def is_code(block):
    list_of_markdown = block.split("\n")
    if list_of_markdown[0][0:3] == "```":
        for line in list_of_markdown:
            if line[0:3] != "```" or line[-3:] != "```":
                return False
        return True
    
def is_quote(block):
    list_of_markdown = block.split("\n")
    if list_of_markdown[0][0] == ">":
        for line in list_of_markdown:
            if line[0] != ">":
                return False
        return True
    
def is_unordered_list(block):
    list_of_markdown = block.split("\n")
    if list_of_markdown[0][0:2] == "* " or list_of_markdown[0][0:2] == "- ":
        for line in list_of_markdown:
            stripped_line = line.lstrip(" ")
            if stripped_line[0:2] != "* ":
                if stripped_line[0:2] != "- ":
                    return False
        return True
def is_orderedlist(block):
    list_of_markdown = block.split("\n")
    if list_of_markdown[0][0].isdigit():
        for line in list_of_markdown:
            stripped_line = line.lstrip(" ")
            count = 0
            for char in stripped_line:
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
    if is_heading(block_of_markdown):
        return "heading"
    if is_code(block_of_markdown):
        return "code"
    if is_quote(block_of_markdown):
        return "quote"
    if is_unordered_list(block_of_markdown):
        return "unordered list"
    if is_orderedlist(block_of_markdown):
        return "ordered list"
    # Didn't find supported type so default to paragraph
    else:
        return "paragraph"

def heading_block_to_html_node(line):
    count = 0
    for char in line:
        if "#" == char:
            count += 1
        else:
            break
    return ParentNode(f"h{count}", list(map(lambda x: x.text_node_to_html_node(), text_to_textnodes(line.lstrip("# ")))))


def paragraph_block_to_html_node(block):
    lines = block.split("\n")
    new_list = []
    for line in lines:
        for htmlnode in list(map(lambda x: x.text_node_to_html_node(), text_to_textnodes(line))):
            new_list.append(htmlnode)
    return ParentNode("p", new_list)

def code_block_to_html_node(block):
    return ParentNode(f"pre", [LeafNode("code", block.strip("`"))])

def quote_block_to_html_node(block):
    lines = block.split("\n")
    new_list = []
    for line in lines:
        new_list.append(ParentNode(f"p", list(map(lambda x: x.text_node_to_html_node(), text_to_textnodes(line.lstrip("> "))))))
    return ParentNode(f"blockquote", new_list)


def unordered_list_to_html_node(block):
    lines = block.split("\n")
    new_list = []
    count = 0
    while count < len(lines):
        line = lines[count]
        new_line = line[2:]
        if line != lines[0]:
            if line.startswith("\t") or line.startswith("    "):
                nested_level = len(line.split("    "))
                node, index = nested_list_helper("\n".join(lines[count:]), "unordered", nested_level, count)
                parent_node = new_list.pop()
                if isinstance(parent_node, ParentNode):
                    parent_node.children.append(node)
                    new_list.append(parent_node)
                else:
                    new_list.append(ParentNode(f"ul", [LeafNode(value=parent_node.value), node]))
                count = index
                continue
        nested_level = 0
        new_list.append(ParentNode(f"li", list(map(lambda x: x.text_node_to_html_node(), text_to_textnodes(new_line)))))
        count += 1
    return ParentNode(f"ul", new_list)

def ordered_list_to_html(block):
    lines = block.split("\n")
    new_list = []
    count = 0
    while count < len(lines):
        line = lines[count]
        new_line = line[3:]
        nested_level = 0
        if line != lines[0]:
            if line.startswith("\t") or line.startswith("    "):
                nested_level = len(line.split("    "))
                node, index = nested_list_helper("\n".join(lines[count:]), "ordered", nested_level, count)
                parent_node = new_list.pop()
                if isinstance(parent_node, ParentNode):
                    parent_node.children.append(node)
                    new_list.append(parent_node)
                else:
                    new_list.append(ParentNode(f"ol", [LeafNode(value=parent_node.value), node]))
                count = index
                continue
        new_list.append(ParentNode(f"li", list(map(lambda x: x.text_node_to_html_node(), text_to_textnodes(new_line)))))
        count += 1
    return ParentNode(f"ol", new_list)

def nested_list_helper(text, list_type, nested_level, index):
    lines = text.split("\n")
    new_list = []
    new_index = index
    num = 0
    tag_text = ""
    if list_type == "ordered":
        num = 3
        tag_text = "ol"
    if list_type == "unordered":
        num = 2
        tag_text = "ul"

    i = 0
    while i < len(lines):
        current_level = len(lines[i].split("    "))
        if lines[i].startswith("    ") or lines[i].startswith("\t"):
            if current_level == nested_level:
                if len(text_to_textnodes(lines[i].lstrip("    ")[num:])) > 1:
                    new_list.append(ParentNode(f"li", list(map(lambda x: x.text_node_to_html_node(), text_to_textnodes(lines[i].lstrip("    ")[num:])))))
                else:
                    new_list.append(LeafNode("li", lines[i].lstrip("    ")[num:]))
                new_index += 1
                i += 1
            elif current_level > nested_level:
                node, end_index = nested_list_helper("\n".join(lines[new_index-1:]), list_type, current_level, new_index)
                leaf = new_list.pop()
                new_list.append(ParentNode(f"li", [LeafNode(value=leaf.value), node]))
                new_index = end_index
                i = end_index - index
        else:
            break
    return ParentNode(tag_text, new_list), new_index
        
def markdown_to_html(markdown):
    # split into blocks using markdown to blocks function
    blocks = markdown_to_blocks(markdown)
    # loop through the returned list of blocks and determine wwhat type the block is with block to block type function
    html_list = []
    for block in blocks:
        type_of_block = block_to_block_type(block)
        # once you know what type of block you are in, convert that block to an htmlnode. assign the proper children to that block (use an additional function to help with this)
        if type_of_block == "paragraph":
            html_list.append(paragraph_block_to_html_node(block))
        elif type_of_block == "heading":
            html_list.append(heading_block_to_html_node(block))
        elif type_of_block == "code":
            html_list.append(code_block_to_html_node(block))
        elif type_of_block == "quote":
            html_list.append(quote_block_to_html_node(block))
        elif type_of_block == "unordered list":
            html_list.append(unordered_list_to_html_node(block))
        elif type_of_block == "ordered list":
            html_list.append(ordered_list_to_html(block))
    return ParentNode("div", html_list)

