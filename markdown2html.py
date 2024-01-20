#!/usr/bin/python3
import sys
import os
import markdown
"""Converts markdown files to html"""


def convert_markdown_to_html(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as md_file:
            markdown_text = md_file.read()
            html_text = markdown.markdown(markdown_text)

        with open(output_file, 'w', encoding='utf-8') as html_file:
            html_file.write(html_text)

        return 0  # Success

    except FileNotFoundError:
        print(f"Missing {input_file}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    # Check the number of arguments
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py <input_file> <output_file>", file=sys.stderr)
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

