from components.readbook import get_string_from_book
from components.readbook import write_document_names_to_file
from components.saveaudio import save_content_to_mp3

import os
import shutil

def clean():
    shutil.rmtree('documents')
    shutil.rmtree('mp3')

    try:
        os.mkdir("mp3")
    except:
        pass

    try:
        os.mkdir("documents")
    except:
        pass

    try:
        os.mkdir("epub")
    except:
        pass


def get_book_names():
    files = []
    for (dirpath, dirnames, filenames) in os.walk("epub"):
        for filename in filenames:
            if filename.endswith(".epub"):
                files.append(filename.replace(".epub", ""))

    return files   


if __name__ == "__main__":
    clean()
    print("")
    print("Copy all EBooks that you want to convert into the epub sub folder. Important: Currently only epub files are supported.")
    input("When you have finished copying press enter to continue")

    books = get_book_names()

    print("")
    print("Scanning Contents of " + str(len(books)) + " EBook(s)")
    for book in books:
        write_document_names_to_file(book_name=book)

    print("")
    print("EPub files contain multiple files. For each epub file you will now find a text file in the documets sub folder containing the names of these files. Please take a look at each file and remove the lines you of the files you dont want in your audiobook. Normally you fill find files like chapter1, chapter2, etc. In most of the cases you will only want these files.")
    input("If you have finished press Enter to continue...")
    print("")

    for book in books:
        print("Converting ", book,  "... ", sep="", end="", flush=True)
        save_content_to_mp3(book_name=book, content=get_string_from_book(book_name=book))

    print("")
    print("You can now find your audiobooks in the sub folder mp3")