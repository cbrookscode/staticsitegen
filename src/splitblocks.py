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


def paragraph_block_to_html_node(block):
    lines = block.split("\n")
    new_list = []
    for line in lines:
        if len(text_to_textnodes(line)) > 1:
            new_list.append(ParentNode(f"p", text_to_textnodes(line)))
        else:
            new_list.append(LeafNode(f"p", line))
    return new_list

def code_block_to_html_node(block):
    return ParentNode(f"pre", [LeafNode("code", block.strip("`"))])

def quote_block_to_html_node(block):
    lines = block.split("\n")
    new_list = []
    for line in lines:
        if len(text_to_textnodes(line.lstrip("> "))) > 1:
            new_list.append(ParentNode(f"p", list(map(lambda x: x.text_node_to_html_node(), text_to_textnodes(line.lstrip("> "))))))
        else:
            new_list.append(LeafNode(f"p", line.lstrip("> ")))
    return ParentNode(f"blockquote", new_list)


# capture logic for nested lists
def unordered_list_to_html_node(block):
    lines = block.split("\n")
    new_list = []
    for line in lines:
        new_line = line[2:]
        if len(text_to_textnodes(new_line)) > 1:
            new_list.append(ParentNode(f"li", list(map(lambda x: x.text_node_to_html_node(), text_to_textnodes(new_line)))))
        else:
            new_list.append(LeafNode(f"li", new_line))
    return ParentNode(f"ul", new_list)

# capture logic for nested lists
def ordered_list_to_html(block):
    lines = block.split("\n")
    new_list = []
    count = -1
    for line in lines:
        count += 1
        new_line = line[3:]
        if line != lines[0]:
            if line.startswith("\t") or line.startswith("    "):
                remainder = lines[count:]
                nested_list = []
                for r_line in remainder:
                    if r_line.startswith("    ") and not r_line[4].isspace():
                        nested_list.append(r_line)
                new_list[count - 1] = ParentNode(f"li", [LeafNode(value=lines[count - 1][3:]), ordered_list_to_html("\n".join(nested_list))])
        if len(text_to_textnodes(new_line)) > 1:
            new_list.append(ParentNode(f"li", list(map(lambda x: x.text_node_to_html_node(), text_to_textnodes(new_line)))))
        else:
            new_list.append(LeafNode(f"li", new_line))
    return ParentNode(f"ol", new_list)



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
# heading 2
# heading 3

1. With a list
    1. Nested 1
    2. NEsted 2
2. inside of it.
3. oh no!

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

> This is the *first line* item in a list block
> This is **second line** item
> This is another list item

* This is the *first line* item in a list block
- This is **second line** item
- This is another list item
"""

code_block = """```
function sayHello() {
    console.log("Hello");
    console.log("World");
}
```"""

quote = """
> This is the *first line* of a quote block.
> This is the **second line** of the quote block.
"""

print(markdown_to_blocks(test))
ex = markdown_to_blocks(test)
first_block = ex[0]
second_block = ex[1]
third_block = ex[2]
fourth_block = ex[3]
fifth_block = ex[4]
print(f"heading block to html: {heading_block_to_html_node(first_block)}")
print(f"paragraph block to html: {paragraph_block_to_html_node(third_block)}")
print(f"code block to html: {code_block_to_html_node(code_block).to_html()}")
print(f"This is the quote: {quote}")
print(f"quote block to html: {quote_block_to_html_node(fourth_block).to_html()}")
print(f"this is the fifth block: {(fifth_block)}")
print(f"split: {fifth_block.split("\n")[0].lstrip("- ").lstrip("* ")}")
print(f"unordered list block to html: {unordered_list_to_html_node(fifth_block).to_html()}")
print(f"this is the second block: {(second_block)}")
print(f"ordered list block to html: {ordered_list_to_html(second_block).to_html()}")
