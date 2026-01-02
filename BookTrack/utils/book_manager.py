from utils.file_handler import load_books, save_books

def add_book(title, author):
    books = load_books()
    books.append({
        "title": title,
        "author": author,
        "status": "Not Started"
    })
    save_books(books)

def list_books():
    return load_books()

def update_status(index, status):
    books = load_books()
    if 0 <= index < len(books):
        books[index]["status"] = status
        save_books(books)

def delete_book(index):
    books = load_books()
    if 0 <= index < len(books):
        books.pop(index)
        save_books(books)
