import os
import shutil
from splitblocks import markdown_to_html


destination_dir = "/home/taximan529/workspace/github.com/cbrookscode/staticproject/staticsitegen/public"
source_destination_dir = "/home/taximan529/workspace/github.com/cbrookscode/staticproject/staticsitegen/static"

def delete_old_dir_create_new_empty_one_with_same_name(directory):
    shutil.rmtree(directory)
    os.mkdir(directory)

def copy_static_content_to_public(source_dir, destination_directory):
    source_contents = os.listdir(source_dir)
    for item in source_contents:
        if not os.path.isfile(f"{source_dir}/{item}"):
            os.mkdir(f"{destination_directory}/{item}")
            copy_static_content_to_public(f"{source_dir}/{item}", f"{destination_directory}/{item}")
            continue
        else:
            shutil.copy(f"{source_dir}/{item}", destination_directory)

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("#"):
            if line[1] == " ":
                return line.strip("# ")
    raise Exception("There is no h1 header in the provided markdown")


def generate_page(from_path, template_path, dest_path):
    print("Generating page from from_path to dest_path using template_path")
    with open(from_path, 'r') as f:
        markdown_file = f.read()
        html_string = markdown_to_html(markdown_file).to_html()
        title = extract_title(markdown_file)
        with open(template_path, 'r') as d:
            template_file = d.read()
            title_changed = template_file.replace("{{ Title }}", title)
            new_index_html_file = title_changed.replace("{{ Content }}", html_string)
            with open(f"{dest_path}/index.html", 'w') as e:
                e.write(new_index_html_file)
    
