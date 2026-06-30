class Book:
    def __init__(self, title, genre, rating):
        self.__title = title       
        self.__genre = genre
        self.__rating = rating

    def get_title(self):
        return self.__title

    def get_genre(self):
        return self.__genre

    def get_rating(self):
        return self.__rating

    
    def display(self):
        print(f"{self.__title} ({self.__genre}) Rating: {self.__rating}")


class EBook(Book):
    def __init__(self, title, genre, rating, file_size):
        super().__init__(title, genre, rating)
        self.file_size = file_size

    def display(self):
        super().display()
        print(f"File Size: {self.file_size} MB")

class User:
    def __init__(self, name, favorite_genre):
        self.__name = name
        self.__favorite_genre = favorite_genre

    def get_favorite_genre(self):
        return self.__favorite_genre

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        print("\nLibrary Books:")
        for book in self.books:
            book.display()

    def recommend_books(self, user):
        print("\nRecommended Books:")
        for book in self.books:
            if book.get_genre().lower() == user.get_favorite_genre().lower():
                print(book.get_title())


def main():
    lib = Library()

    lib.add_book(Book("Harry Potter", "Fantasy", 5))
    lib.add_book(Book("Data Structures", "Education", 4))
    lib.add_book(EBook("AI Basics", "Technology", 5, 2.5))

    user = User("Bhavya", "Fantasy")

    lib.display_books()

    lib.recommend_books(user)

main()