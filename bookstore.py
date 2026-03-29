# Информационная система книжного магазина
# Версия 1.0

class Book:
    def __init__(self, title, author, price, quantity):
        self.title = title
        self.author = author
        self.price = price
        self.quantity = quantity

class Bookstore:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
        print(f"Книга '{book.title}' добавлена")
    
    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None
    
    def sell_book(self, title):
        book = self.search_book(title)
        if book and book.quantity > 0:
            book.quantity -= 1
            print(f"Книга '{book.title}' продана")
        else:
            print("Книга отсутствует")

# Пример использования
if name == "__main__":
    store = Bookstore()
    book1 = Book("Война и мир", "Лев Толстой", 500, 10)
    store.add_book(book1)
    store.sell_book("Война и мир")