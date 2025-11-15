import os
from blocks import markdown_to_html_node


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.strip().startswith("# "):
            return line.strip()[2:]
        
    raise Exception("No h1 header found")

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    file = open(from_path)
    markdown = file.read()
    file.close()
    file = open(template_path)
    template = file.read()
    file.close()
    title = extract_title(markdown)
    html = markdown_to_html_node(markdown).to_html()
    full_html = template.replace("{{ Title }}", title).replace("{{ Content }}", html)
    full_html = full_html.replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(full_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    content_files = os.listdir(dir_path_content)
    
    for file in content_files:
        file_or_folder = os.path.join(dir_path_content, file)
        if os.path.isfile(file_or_folder):
            generate_page(file_or_folder, template_path, os.path.join(dest_dir_path, os.path.splitext(file)[0] + ".html"), basepath)
        else:
            generate_pages_recursive(file_or_folder, template_path, os.path.join(dest_dir_path, file), basepath)