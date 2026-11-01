"""
Bookstore Inventory API Client
Performs GET, POST, PUT, DELETE against a mockapi.io books resource.
"""

import requests
from typing import Dict, Any

# ------------------------------------------------------------------
# 1. Replace this with the real URL from your mockapi.io project
# ------------------------------------------------------------------
API_URL = "https://6ae7168d56b2ee1e544018b6.mockapi.io/api/v1/books"


# ------------------------------------------------------------------
# Bonus: Individual functions for each operation
# ------------------------------------------------------------------

def get_books() -> None:
    """GET all books. Prints JSON + status code. Handles HTTP errors."""
    try:
        response = requests.get(API_URL)
        response.raise_for_status()          # raises HTTPError for 4xx/5xx
        print("=== GET all books ===")
        print("Status code:", response.status_code)
        print("Response JSON:")
        print(response.json())
        print()
    except requests.exceptions.HTTPError as e:
        print("HTTP error occurred while fetching books:", e)
        print("Status code:", e.response.status_code if e.response else "N/A")
        print()


def add_book(book: Dict[str, Any]) -> None:
    """POST a new book. Expects status 201."""
    try:
        response = requests.post(API_URL, json=book)
        response.raise_for_status()
        print("=== POST new book ===")
        print("Status code:", response.status_code)   # should be 201
        print("Created book:")
        print(response.json())
        print()
    except requests.exceptions.HTTPError as e:
        print("HTTP error occurred while adding book:", e)
        print()


def update_book(book_id: str, book: Dict[str, Any]) -> None:
    """PUT (replace) an existing book by id."""
    url = f"{API_URL}/{book_id}"
    try:
        response = requests.put(url, json=book)
        response.raise_for_status()
        print(f"=== PUT update book id={book_id} ===")
        print("Status code:", response.status_code)
        print("Updated book:")
        print(response.json())
        print()
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred while updating book {book_id}:", e)
        print()


def delete_book(book_id: str) -> None:
    """DELETE a book by id, then try to GET it to confirm it's gone."""
    url = f"{API_URL}/{book_id}"
    try:
        # Perform the DELETE
        response = requests.delete(url)
        response.raise_for_status()
        print(f"=== DELETE book id={book_id} ===")
        print("Status code:", response.status_code)
        print("Delete response:", response.text or "(empty)")
        print()

        # Immediately try to GET the same id → should fail
        print(f"=== Confirming deletion: GET book id={book_id} ===")
        get_response = requests.get(url)
        get_response.raise_for_status()   # this should raise
        print("Unexpected: book still exists!")
        print(get_response.json())
    except requests.exceptions.HTTPError as e:
        print("As expected, GET after DELETE failed.")
        print("Status code:", e.response.status_code if e.response else "N/A")
        print("Error message:", e)
        print()


# ------------------------------------------------------------------
# Main execution flow (calls the functions above)
# ------------------------------------------------------------------

if __name__ == "__main__":
    # a) GET all books
    get_books()

    # b) POST a 6th book
    new_book = {
        "title": "The Pragmatic Programmer",
        "author": "Andrew Hunt & David Thomas",
        "rating": "10"
        # note: mockapi.io will usually auto-generate the id
    }
    add_book(new_book)

    # c) PUT – update an existing book (change the id to one that exists)
    book_to_update = "1"          # <-- change this to a real id from your data
    updated_data = {
        "title": "Atomic Habits (Updated Edition)",
        "author": "James Clear",
        "rating": "10"
    }
    update_book(book_to_update, updated_data)

    # d) DELETE a book, then confirm with GET
    book_to_delete = "2"          # <-- change this to a real id you want to remove
    delete_book(book_to_delete)

    # Optional: final GET to see the remaining books
    print("=== Final list of books ===")
    get_books()
