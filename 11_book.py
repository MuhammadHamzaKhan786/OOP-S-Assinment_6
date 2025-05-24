class Book:
    total_books = 0 #class variable

    @classmethod
    def increment_book_count(cls):
        cls.total_books +=1

if __name__ == "__main__":
    Book.increment_book_count()
    Book.increment_book_count()

    print(f"Total books added: {Book.total_books} ")    
        