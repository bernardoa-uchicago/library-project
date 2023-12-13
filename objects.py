class book:

    def __init__(name, path, self):
        self.name = None
        self.path = None

    def set_name(self, name):
        self.name = name

    def set_path(self, path):
        self.path = path

class library:

    def __init__(self, name):
        self.library_name = name
        self.book_list = []

    def add_book(self, book):
        self.book_list.append(book)

    def remove_book(self, name):
        if len(self.book_list) == 0:
            print("Empty List")
            return False
        for book in self.book_list:
            if book.name == name:
                self.book_list.remove(book)
                return True
        print("Book name not in list")
        return False
        