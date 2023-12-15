import os
import manager
import shutil
from objects import book, library

help_str = """~To use the library app, simply type any of the words listed below~

- help : Prints this message to the screen

- open {book name} : Opens a selected book using preview. Prompts an error message if book doesn't exist

- add {book path} : Adds a new book to the program. Prompts an error message if given an invalid path 

- delete {book name} : Moves a select file to the trash. Prompts an error message if book doens't exist

- list : lists all book names within directory

- exit : exits the program
"""
os.system('clear')
entry = "0"
lib = library()
directory_list = os.listdir(path='/Users/bfa/Projects/library-project/books/')

#Adds all files from books into a library object
for file in directory_list:
    new_book = book("books/" + str(file))
    library.add_book(lib,new_book)

#Main loop, takes care of entries
while entry != "exit":
    entry = input("Enter command (type 'help' for options): ")
    print()
    os.system('clear')

    if entry == "help":
        print(help_str)
    
    elif entry[:4] == "open" and len(entry) > 4:
        index = manager.find_book(entry[5:], lib.book_list)
        if index == False:
            print("Book not found\n")
            print(lib)
        else:
            manager.open_book(lib.book_list[index])
    
    elif entry == "open":
        print("You must type 'open' followed by one of the book names below to open a book")
        print("-- Book names are case sensitive --\n")
        print(lib)
    
    elif entry == "add" and len(entry) > 3:
        shutil.move(entry[4:], "/Users/bfa/Projects/library-project/books", copy_function=True)
        new_book = book(entry[4:42])
        control = library.add_book(lib, new_book)
        if control == False:
            print("Book already in directory")
        else:
            print("Success!!!")
            print(lib)

    elif entry == "list":
        print(lib)
    
    elif entry == "exit":
        print("\nThank you for using my app :)\n")
    else:
        print("\nInvalid input, type 'help' for available functions\n")