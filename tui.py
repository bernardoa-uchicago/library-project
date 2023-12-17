import os
import manager
import shutil
from send2trash import send2trash
from objects import book, library

help_str = """~To use the library app, simply type any of the words listed below~

- help : Prints this message to the screen

- open {book name} : Opens a selected book using preview. Prompts an error message if book doesn't exist

- add {book path} : Moves a book to the directory, [DOES NOT COPY]. Prompts an error message if given an invalid path 

- delete {book name} : Moves a select file to the trash. Prompts an error message if book doens't exist

- list : lists all book names within directory

- clear : clears terminal window

- exit : exits the program
"""
os.system('clear')
print("Loading...")
entry = "0"
lib = library()
directory_list = os.listdir(path='/Users/bfa/Projects/library-project/books/')
os.system('clear')

#Adds all files from books into a library object
for file in directory_list:
    if file != ".DS_Store":
        new_book = book("books/" + str(file))
        library.add_book(lib,new_book)

#Main loop, takes care of entries
while entry != "exit":
    #Asks user for inputs
    entry = str.lower(input("Enter command (type 'help' for options): "))
    os.system('clear')

    #handles help call
    if entry == "help":
        print(help_str)
    
    #handles open call
    elif entry[:4] == "open" and len(entry) > 4:
        index = manager.find_book(entry[5:], lib.book_list)
        if index < 0:
            print("\nBook not found, please choose one of the books below")
            print(lib)
        else:
            manager.open_book(lib.book_list[index])
    
    elif entry == "open":
        print("You must type 'open' followed by one of the book names below to open a book")
        print("-- Book names are case sensitive --\n")
        print(lib)
    
    #handles add call
    elif entry[:3] == "add" and len(entry) > 3:
        try:
            shutil.move(entry[4:], "/Users/bfa/Projects/library-project/books")
            new_book = book("books/" + entry.split('/')[-1])
            control = library.add_book(lib, new_book)
            if control == False:
                print("\nBook name already in directory\n")
            else:
                print("\nSuccess!!!\n")
                print(lib)
        except:
            print("\nMake sure your path exists and that there are no typos\n")

    elif entry == "add":
        print("\nMust provide a source path\n")

    #handles delete calls
    elif entry[:6] == "delete" and len(entry) > 6:
        file = "/Users/bfa/Projects/library-project/books/" + entry[7:] + ".pdf"
        print(file)
        send2trash(file)
        library.remove_book(lib, entry[7:])
    
    elif entry == "delete":
        print("Must add a book name to delete from list below")
        print(lib)

    #handles list call
    elif entry == "list":
        print(lib)
    
    #handles exit call
    elif entry == "exit":
        print("\nThank you for using my app :)\n")
    
    #handles clear call
    elif entry == "clear":
        os.system('clear')

    #handles extraneous inputs
    else:
        print("\nInvalid input, type 'help' for available functions\n")