from copy import copy_source_to_destination
from generate_page import generate_pages_recursive

def main():
    copy_source_to_destination('/home/sean/static-site-generator/static', '/home/sean/static-site-generator/public')
    generate_pages_recursive("/home/sean/static-site-generator/content/", "/home/sean/static-site-generator/template.html", "/home/sean/static-site-generator/public/")

main()