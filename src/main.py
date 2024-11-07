from textnode import TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from generatesite import copy_static_content_to_public, delete_old_dir_create_new_empty_one_with_same_name, generate_page

def main():

    destination_dir = "/home/taximan529/workspace/github.com/cbrookscode/staticproject/staticsitegen/public"
    static_source_destination_dir = "/home/taximan529/workspace/github.com/cbrookscode/staticproject/staticsitegen/static"
    markdown_source_destination = "/home/taximan529/workspace/github.com/cbrookscode/staticproject/staticsitegen/content/index.md"
    template_path = "/home/taximan529/workspace/github.com/cbrookscode/staticproject/staticsitegen/template.html"

    delete_old_dir_create_new_empty_one_with_same_name(destination_dir)
    copy_static_content_to_public(static_source_destination_dir, destination_dir)
    generate_page(markdown_source_destination, template_path, destination_dir)


if __name__=="__main__":
    main()