from copy import copy_source_to_destination
import sys
from generate_page import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    copy_source_to_destination(dir_path_static, dir_path_public)
    generate_pages_recursive(dir_path_content, template_path, dir_path_public, basepath)

main()