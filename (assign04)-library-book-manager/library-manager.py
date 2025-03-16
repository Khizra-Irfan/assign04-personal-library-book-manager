import json
import os

data_file = 'library.txt'

def load_library():
    if not os.path.exists(data_file):
        return []
    with open(data_file, 'r') as file:   # Open the file in read mode, 'r' means read
        return json.load(file)

def save_library(library):
    with open(data_file, 'w') as file:    # Open the file in write mode, 'w' means write
        json.dump(library, file, indent=4)

def add_book(library):
    title = input('Enter the title of the book: ')
    author = input('Enter the author of the book: ')
    year = input('Enter the year of the book: ')
    genre = input('Enter the genre of the book: ')
    read = input('Have you read the book? (yes/no): ').lower() == 'yes'
    
    new_book = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read': read
    }
    
    library.append(new_book)
    save_library(library)
    print(f"Book '{title}' added to the library.")

def remove_book(library):
    title = input("Enter the title of the book you want to remove from the library: ").lower()
    initial_length = len(library)
    library = [book for book in library if book['title'].lower() != title]

    if len(library) < initial_length:
        save_library(library)
        print(f"Book '{title}' removed from the library.")
    else: 
        print(f"Book '{title}' not found in the library.")

def search_library(library):
    search_by = input("Search by title or author: ").lower()
    if search_by not in ["title", "author"]:
        print("Invalid choice. Please search by 'title' or 'author'.")
        return

    search_term = input(f"Enter the {search_by}: ").lower()

    results = [book for book in library if search_term in book[search_by].lower()]

    if results:
        for book in results:
            status = "Read" if book['read'] else "Unread"
            print(f"{book['title']} by {book['author']} ({book['year']}) - {status}")
    else:
        print(f"No books found for '{search_term}' in the {search_by} field.")

def display_all_books(library):
    if library:
        for book in library:
            status = "Read" if book['read'] else "Unread"
            print(f"{book['title']} by {book['author']} ({book['year']}) - {status}")
    else:
        print("No books in the library.")

def display_statistics(library):
    total_books = len(library)
    total_read = len([book for book in library if book['read']])
    percentage_read = (total_read / total_books) * 100 if total_books > 0 else 0
    
    print(f"Total books: {total_books}")
    print(f"Total read: {total_read}")
    print(f"Percentage read: {percentage_read:.2f}%")

def main():
    library = load_library()
    while True:
        print("Welcome to the Library Manager!")
        print("\nMenu")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search the library")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_library(library)
        elif choice == "4":
            display_all_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
