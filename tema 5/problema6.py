class LibraryItem:
    def __init__(self, title, author, item_id):
        self.title = title
        self.author = author
        self.item_id = item_id
        self.checked_out = False

    def display_info(self):
        print(f"Item ID: {self.item_id}, Title: {self.title}, Author: {self.author}, Checked Out: {'Yes' if self.checked_out else 'No'}")

    def check_out(self):
        if not self.checked_out:
            print(f"Checked out: {self.title}")
            self.checked_out = True
        else:
            print(f"{self.title} is already checked out.")

    def return_item(self):
        if self.checked_out:
            print(f"Returned: {self.title}")
            self.checked_out = False
        else:
            print(f"{self.title} was not checked out.")


class Book(LibraryItem):
    def __init__(self, title, author, item_id, genre):
        super().__init__(title, author, item_id)
        self.genre = genre

    def display_info(self):
        super().display_info()
        print(f"Type: Book, Genre: {self.genre}")


class DVD(LibraryItem):
    def __init__(self, title, director, item_id, duration):
        super().__init__(title, director, item_id)
        self.director = director
        self.duration = duration

    def display_info(self):
        super().display_info()
        print(f"Type: DVD, Director: {self.director}, Duration: {self.duration} minutes")


class Magazine(LibraryItem):
    def __init__(self, title, publisher, item_id, issue_number):
        super().__init__(title, publisher, item_id)
        self.publisher = publisher
        self.issue_number = issue_number

    def display_info(self):
        super().display_info()
        print(f"Type: Magazine, Publisher: {self.publisher}, Issue Number: {self.issue_number}")


book = Book("The Great Gatsby", "F. Scott Fitzgerald", 1001, "Classic")
book.display_info()
book.check_out()
book.return_item()

dvd = DVD("Inception", "Christopher Nolan", 2001, 148)
dvd.display_info()
dvd.check_out()
dvd.check_out()

magazine = Magazine("National Geographic", "National Geographic Society", 3001, 255)
magazine.display_info()
magazine.check_out()
