# Concert Ticket Booker

def get_user_input(prompt: str) -> str:
    """Prompt the user for input and return a cleaned, non-empty string."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty. Please try again.\n")


def book_ticket(name: str, artist: str) -> str:
    """Generate a booking confirmation message."""
    return f"Hey {name}! Your tickets to see {artist} are booked successfully!"


def main():
    print("Welcome to the Concert Ticket Booker\n")

    name   = get_user_input("What is your name? ")
    artist = get_user_input("Which band/artist would you like to see? ")

    confirmation = book_ticket(name, artist)
    print(f"\n {confirmation}")


if __name__ == "__main__":
    main()