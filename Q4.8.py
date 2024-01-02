# Base class LibraryItem
class LibraryItem:
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.checked_out = False

    def display_info(self):
        print(f"Title: {self.title}\nItem ID: {self.item_id}\nChecked Out: {self.checked_out}")

    def check_out(self):
        if not self.checked_out:
            print(f"{self.title} checked out successfully.")
            self.checked_out = True
        else:
            print(f"{self.title} is already checked out.")

    def check_in(self):
        if self.checked_out:
            print(f"{self.title} checked in successfully.")
            self.checked_out = False
        else:
            print(f"{self.title} is not checked out.")

# Derived class Book
class Book(LibraryItem):
    def __init__(self, title, item_id, author):
        super().__init__(title, item_id)
        self.author = author

    def display_info(self):
        super().display_info()
        print(f"Author: {self.author}")

# Derived class DVD
class DVD(LibraryItem):
    def __init__(self, title, item_id, director):
        super().__init__(title, item_id)
        self.director = director

    def display_info(self):
        super().display_info()
        print(f"Director: {self.director}")

# Derived class Journal
class Journal(LibraryItem):
    def __init__(self, title, item_id, publisher):
        super().__init__(title, item_id)
        self.publisher = publisher

    def display_info(self):
        super().display_info()
        print(f"Publisher: {self.publisher}")

# Example usage:

# Create objects for Book, DVD, and Journal
book1 = Book("Python Programming", "B001", "John Doe")
dvd1 = DVD("Inception", "D001", "Christopher Nolan")
journal1 = Journal("Science Journal", "J001", "Science Publishing")

# Display information for each item
print("\nBook Information:")
book1.display_info()

print("\nDVD Information:")
dvd1.display_info()

print("\nJournal Information:")
journal1.display_info()

# Check out and check in some items
book1.check_out()
dvd1.check_out()
journal1.check_in()
book1.check_out()
dvd1.check_out()
journal1.check_in()
