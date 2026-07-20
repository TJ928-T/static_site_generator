import os
import pathlib
from markdown_to_html import markdown_to_html_node
from extract_title import extract_title
from copy_files_to_dir import clean_directory, copy_files_dir



def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    if os.path.isfile(from_path):
        with open(from_path, "r") as file:
            md = file.read()
        with open(template_path, "r") as file:
            template = file.read()
        node = markdown_to_html_node(md)
        html = node.to_html()
        title = extract_title(md)
        file_template = template.replace("{{ Title }}", title)
        file_template = file_template.replace("{{ Content }}", html)
        dir = os.path.dirname(dest_path)
        if os.path.exists(dir) is False:
            os.makedirs(dir)
        if os.path.exists(dest_path) is False:
            print(dest_path)
            with open(dest_path, "w") as f:
                f.write(file_template)
    else:
        from_paths = os.listdir(from_path)
        for path in from_paths:
            name = path.split(".")
            file_path = os.path.join(from_path, path)
            if "md" in name:
                path = f"{name[0]}.html"
            dest = os.path.join(dest_path, path)
            generate_page(file_path, template_path, dest)



def main():
    clean_directory()
    copy_files_dir("./static", "./public")
    generate_page("./content", "./template.html", "./public")

if __name__ == "__main__":
    main()