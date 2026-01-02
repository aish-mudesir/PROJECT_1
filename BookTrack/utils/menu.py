from utils.book_manager import add_book, list_books, update_status, delete_book

def show_menu():
    while True:
        print("\n📚 BookTrack Menu")
        print("1. Add Book")
        print("2. View Books")
        print("3. Update Status")
        print("4. Delete Book")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Book title: ")
            author = input("Author: ")
            add_book(title, author)
            print("✅ Book added.")

        elif choice == "2":
            books = list_books()
            for i, book in enumerate(books):
                print(f"{i}. {book['title']} - {book['author']} [{book['status']}]")

        elif choice == "3":
            index = int(input("Book index: "))
            status = input("New status (Reading/Completed): ")
            update_status(index, status)
            print("✏️ Status updated.")

        elif choice == "4":
            index = int(input("Book index: "))
            delete_book(index)
            print("🗑️ Book deleted.")

        elif choice == "5":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice.")
