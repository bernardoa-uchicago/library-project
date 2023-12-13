import subprocess
from objects import book, library



def search_book(book, library_list):
    if book in library_list:
        print("Book in library")
        return

def open_book(book):
    try:
        subprocess.run(['open', '-a', 'Preview', book.path])
    except:
        print("Book not found")
        return False
    return

def create_book(name, file_name):
    new = book
    book.set_name(new, name)
    new_path = '/bfa/Projecs/libray-project/books/' + file_name
    book.set_path(new, new_path)
    return new

def create_library(name):
    new = library
    new.name = name
    return new