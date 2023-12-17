import subprocess
from objects import book, library

def find_book(book_name, library_list):
    index = 0
    for i, item in enumerate(library_list):
        if item.name == book_name:
                index = i
                return index
    return -1

def search_book(book_name, library_list):
    for item in library_list:
        if item.name == book_name:
            return True
    return False

def open_book(book):
    try:
        subprocess.run(['open', '-a', 'Preview', str(book.path)])
    except:
        print("Book not found")
        return False
    return True
    