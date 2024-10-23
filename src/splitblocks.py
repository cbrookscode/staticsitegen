

def markdown_to_blocks(markdown):
    if not markdown:
        raise Exception("No Markdown Text Provided")
    final = []
    for block in markdown.split("\n\n"):
        if block.strip():
            final.append(block.strip())
    return final

def block_to_block_type(block_of_markdown):
    if not block_of_markdown:
        raise Exception("No markdown provided!")
    if len(block_of_markdown) == 1:
        return "paragraph"
    split = block_of_markdown.split("\n")

    # Check if heading type
    if block_of_markdown[0] == "#":
        for line in split:
            count = 0
            for i in range(1, 8):
                if line[i] == "#":
                    count += 1
                elif count == 6:
                    return "paragraph"
                elif line[i] == " ":
                    break
                else:
                    return "paragraph"
        return "heading"
            
    # Check if code type
    if block_of_markdown[0:3] == "```":
        for line in split:
            if line[0:3] != "```" or line[-3:] != "```":
                return "paragraph"
        return "code"
    
    # Check if quote type
    if block_of_markdown[0] == ">":
        for line in split:
            if line[0] != ">":
                return "paragraph"
        return "quote"
    
    # Check if unordered list type
    if block_of_markdown[0:2] == "* " or block_of_markdown[0:2] == "- ":
        for line in split:
            if line[0:2] != "* ":
                if line[0:2] != "- ":
                    return "paragraph"
        return "unordered_list"
    
    # Check if ordered list type
    if block_of_markdown[0].isdigit():
        for line in split:
            count = 0
            for char in line:
                if not char.isdigit():
                    if char == ".":
                        if line[count + 1] != " ":
                            return "paragraph"
                        else:
                            break
                    else:
                        return "paragraph"
                else:
                    count += 1
        return "ordered list"
    
    # Didn't find supported type so default to paragraph
    else:
        return "paragraph"