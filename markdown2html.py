#!/usr/bin/python3
""" Converts markdown file to html"""


import sys
import os
import markdown
from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor
from markdown.util import etree


class HeadingExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        md.treeprocessors.register(HeadingTreeprocessor(md), 'heading', 1)


class HeadingTreeprocessor(Treeprocessor):
    def run(self, root):
        for element in root.iter():
            if element.tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                element.tag = 'h' + element.tag[-1]
        return root


def convert_markdown_to_html(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as md_file:
            markdown_text = md_file.read()

        md = markdown.Markdown(extensions=[HeadingExtension()])
        html_text = md.convert(markdown_text)

        with open(output_file, 'w', encoding='utf-8') as html_file:
            html_file.write(html_text)

        return 0  # Success

    except FileNotFoundError:
        print(f"Missing {input_file}", file=sys.stderr)
        return 1


# Check the number of arguments
if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py <input_file> <output_file>",
          file=sys.stderr)
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

# Check if the input file exists
if not os.path.exists(input_file):
    print(f"Missing {input_file}", file=sys.stderr)
    sys.exit(1)

# Convert Markdown to HTML
exit_code = convert_markdown_to_html(input_file, output_file)
sys.exit(exit_code)
