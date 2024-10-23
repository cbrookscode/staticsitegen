

def markdown_to_blocks(markdown):
    if not markdown:
        raise Exception("No Markdown Text Provided")
    final = []
    for block in markdown.split("\n\n"):
        if block.strip():
            final.append(block.strip())
    return final