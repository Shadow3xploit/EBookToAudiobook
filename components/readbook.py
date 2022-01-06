import ebooklib
from ebooklib import epub

def remove_html_markup(s):
    tag = False
    quote = False
    out = ""

    for c in s:
            if c == '<' and not quote:
                tag = True
            elif c == '>' and not quote:
                tag = False
            elif (c == '"' or c == "'") and tag:
                quote = not quote
            elif not tag:
                out = out + c

    return out

def write_document_names_to_file(book_name):
    book = epub.read_epub("epub/" + book_name + ".epub")

    content = ""

    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            content += item.get_name() + "\n"
    
    with open("documents/" + book_name + ".txt", "w") as file:
        file.write(content)

def get_string_from_book(book_name):
    book = epub.read_epub("epub/" + book_name + ".epub")

    wanted_documents = []
    with open("documents/" + book_name + ".txt", "r") as file:
        wanted_documents = file.read().splitlines()

    content = ""

    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT and item.get_name() in wanted_documents:
            content += remove_html_markup(item.get_content().decode("utf-8"))

    return content