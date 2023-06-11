# load all markdown files in the Journal folder

import os
import re

date_pattern = r'\d{4}/\d{2}/\d{2}'


def get_markdown_files(path, skipped_files=['Journal.md']):
    markdown_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".md") and file not in skipped_files:
                # exclude those markdown files without a date in the file path, i.e. not a valid journal entry
                full_path = os.path.join(root, file)
                if re.search(date_pattern, full_path):
                    markdown_files.append(full_path)

    # sort markdown files by date
    # research() returns a match object and match.group() will return the matched date string
    markdown_files.sort(key=lambda x: re.search(
        r'\d{4}/\d{2}/\d{2}', x).group())
    return markdown_files


def write_markdown_files(markdown_files, output_file):
    with open(output_file, "w") as outfile:
        for fname in markdown_files:
            with open(fname) as infile:
                outfile.write(infile.read())
                outfile.write("\n\n")


if __name__ == '__main__':
    journal_folder = os.path.join(os.path.expanduser("~"), "Journal")
    markdown_files = get_markdown_files(journal_folder)

    # write the markdown files to a single output file
    write_markdown_files(markdown_files, os.path.join(
        journal_folder, "Journal.md"))
