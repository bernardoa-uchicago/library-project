class book:

    def __init__(self, path):
        self.name = path[6:-4]
        self.path = path

    def set_name(self, name):
        self.name = name

    def set_path(self, path):
        self.path = path

    def __str__(self):
        return f"Book name: {self.name}"

class library:

    def __init__(self):
        self.book_list = []

    def add_book(self, book):
        if book not in self.book_list:
            self.book_list.append(book)
            return True
        return False

    def remove_book(self, name):
        if len(self.book_list) == 0:
            return False
        for book in self.book_list:
            if book.name == name:
                self.book_list.remove(book)
                return True
        return False
        
    def __str__(self):
        string = "Books:"
        for book in self.book_list:
            string = string + "\n" + str(book.name)
        return string + "\n"

